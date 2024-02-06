const fs = require('fs');
const path = require('path');
const klawSync = require('klaw-sync');
const COS = require('@tencent/cosapi');
const SecretId = 'p9Lx2y0W36cpYGwf8A3jxC6y';
const SecretKey = 'Axl6OKQMZTf5QHoj3gJTsvxtLm4r0wfA1A';
const host = 'gzc.vod.tencent-cloud.com';
const blackListFiles = ['FEDhUbUPLOADSCRIPT.js','FEDHUBtrIggerInfoRecord.js'];
const xml2js = require('xml2js');
const builder = new xml2js.Builder();

(async () => {
  const cos = new COS({
    secretID: SecretId,
    secretKey: SecretKey,
    appid: 75028,
    host,
    ServiceDomain: 'service.gzc.vod.tencent-cloud.com',
    Domain: '{Bucket}-75028.gzc.vod.tencent-cloud.com',
  });
  const resultDir = './dist';
  const base = path.resolve(__dirname, resultDir);
  let files = [];
  try {
    files = klawSync(base, { nodir: true, filter: ()=>true }).map(item => item.path.replace(base, ''));
  } catch (e) {
    console.log('爬文件失败', e);
    files = klawSync(base, { nodir: true }).map(item => item.path.replace(base, ''));
  }
  files = files.filter(p => {
    const parts = p.split('/').filter(item => item);
    const isBanned = parts.some(item => blackListFiles.indexOf(item) > -1);
    console.log(p, 'is banned:', isBanned);
    return !isBanned;
  });
  const fileCount = files.length;
  const batchSize = 100;
  let currentCount = 0;
  let pms = [];
  for (const p of files) {
    pms.push(new Promise((resolve, reject) => {
      const commOpt = {
        method: 'put',
        bucket: 'webcdn',
        body: fs.readFileSync(path.join(base, p)),
      };
      const uri = path.join('/wxalbumgroup/devdist', '', p);
      cos.run({
        ...commOpt,
        uri,
      }).then((res) => {
        console.log('成功上传这个文件', uri, path.join(base, p));
        resolve(res);
      })
        .catch((e) => {
          console.log('上传文件失败', e, uri, path.join(base, p));
          reject(e);
        });
    }));
    currentCount += 1;
    if ((currentCount % batchSize === 0) || (currentCount === fileCount)) {
      await Promise.all(pms);
      pms = [];
    }
  }
  const preserveKeys = files.map(p => path.join('/wxalbumgroup/devdist', '', p));
  // 上传完之后，看看是不是全量发布，全量发布就删掉不需要的文件
  if (0 === 1) {
    console.log('使用全量模式发布，需要先删除原有文件');
    const getAndClean = async (marker) => {
      const endpointPrefix = path.join('/wxalbumgroup/devdist', '');
      const BUCKETNAME = 'webcdn';
      const parameters = {
        prefix: endpointPrefix,
      };
      if (marker) {
        parameters.marker = '/' + BUCKETNAME + marker;
      }
      const listResp = await cos.run({
        method: 'get',
        bucket: BUCKETNAME,
        parameters,
      });
      let keys = [];
      let rawLen = 0;
      let lastKey;
      console.log({
        parameters,
        // listResp: JSON.stringify(listResp),
      });
      try {
        keys = listResp.result.LISTBUCKETRESULT.CONTENTS.map(item => path.join(endpointPrefix, item.KEY[0]));
        rawLen = keys.length;
        lastKey = listResp.result.LISTBUCKETRESULT.NEXTMARKER || keys[rawLen - 1];
        keys = keys.filter(k => !preserveKeys.includes(k));
      } catch (e) {
        console.log('获取cos上的文件列表失败', e);
        if (listResp.statusMessage === 'OK') {
          console.log('实际上，文件可能可能已经到了尽头，所以CONTENTS为空', JSON.stringify(listResp));
        }
      }
      const keysLength = keys.length;
      if (keysLength > 0) {
        console.log('开始删除文件');
        const deleteResult = await cos.run({
          method: 'POST',
          uri: '/',
          bucket: BUCKETNAME,
          parameters: { delete: '' },
          body: builder.buildObject({
            Delete: {
              Object: keys.map(k => ({ Key: k })),
            },
          }),
        });
        console.log('文件删除结果:', deleteResult);
      }
      console.log('这次删除了这么多文件', {
        keysLength,
        rawLen,
        lastKey,
      });
      return {
        needDelCount: rawLen,
        lastKey,
      };
    };
    let needDelCount = 1;
    let lastKey;
    while (!(needDelCount < 1)) {
      const result = await getAndClean(lastKey);
      needDelCount = result.needDelCount;
      lastKey = result.lastKey;
    }
  }
  process.exit();
})();