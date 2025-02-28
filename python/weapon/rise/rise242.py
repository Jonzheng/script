import requests, json, time, re
from bs4 import BeautifulSoup, element
host = 'https://gamecat.fun'
tag = '结算道具'
link = 'https://gamecat.fun/rise/zh/index.php?title=' + tag + '/'
def getItemList():
  with open(r'D:\pro\script\python\weapon\html\242.html', 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    items = []
    tree = ''
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 7:
        tee = tds[0].get_text().strip()
        if '衍生' in tee:
          tee = re.sub(r"[a-zA-Z]", "", tee)
          tee = tee.replace('\'', '').replace('&', '').replace('-', '').strip()
          tree = tee
        for td in tds:
          arr = td.select('a')
          if len(arr) > 0:
            wp = arr[0].get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
            if wp:
              suf = arr[0]['href']# 械・大
              # print('__', tree, wp)
              items.append([wp, tree, suf])
    return items
wht = ['#ff0000', '#fd7e0f', '#fffb00', '#3ad00c', '#2368ff', '#ffffff', '#000000']
wpNames = []
def scraftItem(name, link):
  resp = requests.get(link)
  soup = BeautifulSoup(resp.text, 'lxml')
  tableTag = soup.find_all(name='table')
  parent = soup.find('div', class_='mw-parser-output')
  desc = ''
  sk = ''
  for pp in parent.children:
    if pp.name == 'p':
      pt = pp.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
      if sk:
        desc = pt
        sk = ''
      if '使用本武器进行配装' in pt:
        sk = 1
  print(link)
  idx = 0
  base = []
  raty = []
  finds = []
  ques = []
  crafts = []
  ways = []
  slot = ''
  d_slot = ''
  d_slot = ''
  d_sk = ''
  nrr = []
  wimg = ''
  for tb in tableTag:
    th = tb.select('th')
    if len(th) > 0:
      thh = th[0].get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
      for tbd in tb.select('tbody'):
        idx += 1
        print('___idx', idx, thh)
        if name == thh:
          trs = tbd.select('tr')
          tds = trs[1].select('td')
          if len(tds) > 0:
            img = tds[0].select('a img')
            # print('__', img[0]['src'])
            if len(img) > 0:
              wimg = img[0]['src']
        elif '中文简体' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 4:
              [td1, td2, td3, td4] = tds
              # name = td1.get_text().replace('\r', '').replace('\n', '').strip()
              hk = td2.get_text().replace('\r', '').replace('\n', '').strip()
              en = td3.get_text().replace('\r', '').replace('\n', '').strip()
              jp = td4.get_text().replace('\r', '').replace('\n', '').strip()
              base = [name, hk, en, jp]
              print('_base', base)
        elif '稀有度' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) > 6:
              [td1, td2, td3, td4, td5, td6] = tds[:6]
              rare = td1.get_text().replace('\r', '').replace('\n', '').strip()
              att = td2.get_text().replace('\r', '').replace('\n', '').strip()
              dff = td3.get_text().replace('\r', '').replace('\n', '').strip()
              ele = td4.get_text().replace('\r', '').replace('\n', '').strip()
              aff = td5.get_text().replace('\r', '').replace('\n', '').strip()
              if rare:
                d6 = td6.select('tr')
                wtr = []
                for dr in d6:
                  ed = []
                  cmp = {}
                  for p in dr.select('td'):
                    width = ''
                    color = ''
                    width_match = re.search(r'width:(\d+)px', p['style'])
                    if width_match:
                      width = width_match.group(1)
                    color_match = re.search(r'background-color:#[0-9a-fA-F]{6}', p['style'])
                    if color_match:
                      color = color_match.group(0).split(':')[1].strip()
                    # print(width, color)
                    cmp[color] = width
                  for k in wht:
                    wt = cmp.get(k, '0')
                    wt = int(int(wt) * 400 / 160)
                    ed.append(str(wt))
                  # print('_ed', ed)
                  wtr.append(','.join(ed))
                print('_rare', [rare, att, dff, aff, ele])
                print('_whet', '|'.join(wtr))
                raty = [rare, att, dff, aff, ele, '|'.join(wtr)]
        elif '饰品槽' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) > 1:
              ta1 = tds[0].select('a')
              ta2 = tds[1].select('a')
              a1 = []
              a2 = []
              for ta in ta1:
                st = ta['title'].replace('-star', '').replace('no', '').strip()
                if st:
                  a1.append(st)
              for ta in ta2:
                st = ta['title'].replace('-star', '').replace('no', '').strip()
                if st:
                  a2.append(st)
              # print('__slot', a1, a2)
              slot = ','.join(a1)
              d_slot = ','.join(a2)
            if len(tds) > 2:
              a3 = []
              p2 = tds[2].select('p')
              for p in p2:
                it = p.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
                if it:
                  a3.append(it)
              d_slot = tds[1].get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
              d_sk = ','.join(a3)
            print('_slot', slot)
            print('_d_slot', d_slot)
            print('_dsk', d_sk)
        elif '衍生方式' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 7:
              [td1, td2, td3, td4, td5, td6, td7] = tds
              d1 = td1.get_text().replace('\r', '').replace('\n', '').strip()
              wpn = td2.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
              if wpn == name:
                buy = td5.get_text().replace('\r', '').replace('\n', '').strip()
                d6 = td6.select('p')
                d7 = td7.select('p')
                print('__d1', d1)
                print('__buy', buy)
                zenny = ''
                unlock = ''
                dr6 = []
                create = '0'
                if '生产' in d1:
                  create = '1'
                if len(d6) > 0:
                  for p in d6:
                    it = p.get_text().replace('\r', '').replace('\n', '').replace(' ', '').replace('x', ':').strip()
                    if it.isdigit():
                      zenny = it
                    elif '获得' in it:
                      unlock = it.replace('获得', '').replace('【', '').replace('】', '')
                    else:
                      dr6.append(it)
                    print('____p6', it)
                  crafts.append([name, '|'.join(dr6), unlock, zenny, buy, create])
                if len(d7) > 0:
                  for p in d7:
                    it = p.get_text().replace('\r', '').replace('\n', '').replace(' ', '').replace('x', ':').strip()
                    if it.isdigit():
                      zenny = it
                    elif '获得' in it:
                      unlock = it.replace('获得', '').replace('【', '').replace('】', '')
                    else:
                      dr6.append(it)
                    print('____p7', it)
                  crafts.append([name, '|'.join(dr6), unlock, zenny, buy, create])
            elif len(tds) == 6:
              [td1, td2, td3, td4, td5, td6] = tds
              d2 = td2.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
              print('_____next', d2)
              nrr.append(d2)
  return [base, raty, slot, d_slot, d_sk, desc, nrr, wimg, crafts]

with open(r'D:\pro\script\python\weapon\data2\base2423.txt', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\weapon\data2\wimg2423.txt', 'w', encoding='utf-8') as out2:
    with open(r'D:\pro\script\python\weapon\data2\cft2423.txt', 'w', encoding='utf-8') as out3:
      items = getItemList()
      for irr in items[200:]:
        [wp, tree, suf] = irr
        print('_tree', tree)
        [base, raty, slot, d_slot,d_sk,desc, nrr, wimg, crafts] = scraftItem(wp, host + suf)
        [name, hk, en, jp] = base
        [rare, att, dff, aff, ele, whet] = raty
        line1 = '\t'.join(base + raty + [tree, slot, d_slot, d_sk,desc, '|'.join(nrr)])
        out.write(line1+'\n')
        line1 = '\t'.join([name, wimg])
        out2.write(line1+'\n')
        for crf in crafts:
          line1 = '\t'.join(crf)
          out3.write(line1+'\n')
        time.sleep(2)
