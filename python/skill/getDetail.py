import requests, json, time
from bs4 import BeautifulSoup
skillArr = []
skillArr2 = []
faArr = {}
def getItem(url, skiName):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  suit = 0
  max_level = 1
  desc = ''
  color = 1
  lvArr = []
  for cd in cards:
    tn = ''
    head = cd.select('.card-header')
    ctext = cd.select('.card-text')
    if ctext:
      desc = ctext[0].get_text().replace('\r', '').replace('\n', '').strip()
    hasImg = []
    if head:
      tn = head[0].get_text().strip()
      hasImg = head[0].select('img')
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if len(hasImg) > 0:
      icons = hasImg[0]['style'].split(';')
      color = icons[0].split('/')[-1].split('.')[0]
      for tr in trs:
        th1 = tr.select('th')[0].get_text().strip()
        td1 = tr.select('td')[0]
        if '系列技能' in th1:
          suit = td1.get_text().strip()
        if 'max_level' in th1:
          max_level = td1.get_text().strip()
    elif 'Level' in th:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 3:
          [td1, td2, td3] = tds
          lv = td1.get_text().strip()
          desc2 = td2.get_text(':').replace('\r', '').replace('\n', '').strip()
          desc2 = desc2.replace(':（', '（')
          params = td3.get_text().strip()
          print(lv, ':', params)
          print('desc2', desc2)
          lvArr.append(';'.join([lv, desc2, params]))
          if ':' in desc2:
            [sname, desc3] = desc2.split(':')
            skillArr2.append([sname, 2, desc3, lv, 0, ''])
            if faArr.get(sname) and skiName not in faArr.get(sname):
              faArr[sname].append(skiName)
            else:
              faArr[sname] = [skiName]

  skillArr.append([skiName, suit, desc, max_level, color, '|'.join(lvArr)])


names = []
with open(r'D:\git_me\script\python\skill\data\list.json', 'r', encoding='utf-8') as inf:
  list = json.loads(inf.readlines()[0])
  for arr in list:
    print('arr', arr)
    [name, url] = arr
    url = 'https://mhw.poedb.tw' + url
    getItem(url, name)
    time.sleep(1)
  with open(r'D:\git_me\script\python\skill\data\t_skill2.sql', 'w', encoding='utf-8') as out:
    for ski in skillArr:
      n = ski[0]
      parents = ''
      if faArr.get(n):
        parents = '|'.join(faArr.get(n))
      ski.append(parents)
      names.append(n)
      [skiName, type, desc, max_level, color, lv_detail, suits] = ski
      sql = "insert into t_skill values (null, '{}', '{}', {}, {}, {}, '{}', '{}')".format(skiName, desc, max_level, type, color, lv_detail, suits)
      out.write(sql+';\n')
      # out.write(json.dumps(ski, ensure_ascii=False) + '\n')
    for ski in skillArr2:
      n = ski[0]
      if n not in names:
        parents = ''
        if faArr.get(n):
          parents = '|'.join(faArr.get(n))
        ski.append(parents)
        names.append(n)
        print('-', ski)
        [skiName, type, desc, max_level, color, lv_detail, suits] = ski
        sql = "insert into t_skill values (null, '{}', '{}', {}, {}, {}, '{}', '{}')".format(skiName, desc, max_level, type, color, lv_detail, suits)
        out.write(sql+';\n')
        # out.write(json.dumps(ski, ensure_ascii=False) + '\n')
  # with open(r'D:\git_me\script\python\skill\data\t_skill0.sql', 'w', encoding='utf-8') as out:
  #   for chm in skillArr:
  #     [skiName, suit, desc, max_level, color] = chm
  #     if not name in names:
  #       names.append(name)
  #       print('chm', chm)
  #       sql = "insert into t_skill values (null, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name, rarity, desc, skill, craft, unlock, pre, next, color)
  #       out.write(sql+';\n')
  #   for line in sqls:
  #     out.write(line+';\n')

