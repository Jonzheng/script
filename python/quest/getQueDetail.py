import requests, json, time
from bs4 import BeautifulSoup
questArr = []
def getItem(url, questName, rank, stage, icon, monEn):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  target = ''
  zenny = 1
  skill = ''
  failCondit = ''
  client = ''
  timeLimit = 30
  rewards = ''
  name_en = ''
  name_jp = ''
  minRank = ''
  for cd in cards:
    tn = ''
    head = cd.select('.card-header')
    hasImg = []
    if head:
      tn = head[0].get_text().strip()
      hasImg = head[0].select('img')
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if '任务报酬' in tn:
      arr = []
      for tr in trs:
        tds = tr.select('td')
        if len(tds) > 1:
          [td1, td2] = tds
          item = td1.get_text().replace('x', ':').replace(' ', '').replace('\'', '.').strip()
          percent = td2.get_text().replace('Guaranteed', '保底').strip()
          print(item, percent)
          arr.append(item+':'+percent)
      rewards = '|'.join(arr)
    elif len(hasImg) > 0:
        for tr in trs:
          th1 = tr.select('th')[0].get_text().strip()
          td1 = tr.select('td')[0]
          if 'TARGET' in th1:
            target = td1.get_text().strip()
          if '失败条件' in th1:
            failCondit = td1.get_text().replace('\r', '').replace('\n', '|').strip()
          if '委托人' in th1:
            client = td1.get_text(":").replace(':\r', '').replace('\n', '').strip().strip(':')
          if '生态地图' in th1:
            stage = td1.get_text().strip()
          if '报酬金' in th1:
            zenny = td1.get_text().replace('zenny', '').strip()
          if '限制时间' in th1:
            timeLimit = td1.get_text().replace(' Minute', '').strip()
          if '承接/参加条件' in th1:
            minRank = td1.get_text().replace('hunterrank', '').strip()
    if '语言' in tn:
      name_jp = trs[0].select('td')[0].get_text().strip()
      name_en = trs[1].select('td')[0].get_text().replace('\'', '·').strip()
      name = trs[8].select('td')[0].get_text().strip()
      print(name, name_en, name_jp)
  questArr.append([rank, icon, questName, minRank, zenny, timeLimit, skill, stage, client, target, failCondit, monEn, rewards, name_en, name_jp])
  print([rank, icon, questName, minRank, zenny, timeLimit, skill, stage, client, target, failCondit, monEn, rewards, name_en, name_jp])


names = []
with open(r'D:\git_me\script\python\quest\data\Arena.json', 'r', encoding='utf-8') as inf:
  list = json.loads(inf.readlines()[0])
  for arr in list:
    print('arr', arr)
    [name, url, rank, stage, icon, monEn] = arr
    url = 'https://mhw.poedb.tw' + url
    chm = getItem(url, name, rank, stage, icon, monEn)
    time.sleep(2)
  with open(r'D:\git_me\script\python\quest\data\Arena.txt', 'w', encoding='utf-8') as out:
    for brr in questArr:
      out.write(json.dumps(brr, ensure_ascii=False)+'\n')

