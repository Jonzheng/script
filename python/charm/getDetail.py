import requests, json, time
from bs4 import BeautifulSoup
charmArr = []
def getItem(url, chmName):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  preCharm = ''
  rarity = 1
  skill = ''
  craft = ''
  nextCharm = ''
  unlock = ''
  desc = ''
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
    if 'Usage' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        [td1, td2] = tds
        create = ''
        type = td1.get_text().strip()
        if '强化' in type:
          preCharm = td1.select('a')[0].get_text().strip()
        elif 'Upgrade' in type:
          aaa = td1.select('a')[0]
          nextCharm = aaa.get_text().strip()
          url = 'https://mhw.poedb.tw' + aaa['href']
          getItem(url, nextCharm)
        elif '生产' in type:
          create = 1
        component = td2.get_text('|').replace('\r', '').strip().replace('| x', '')
        if preCharm or create:
          # insert into t_wp_craft values ('foo', 1),('bar', 2);
          # component 毒妖鸟的喉袋 1|毒妖鸟的尾巴 2|大地结晶 4|水晶原石 1|Unlock: |毒妖鸟
          cps = component.replace('Unlock: |', 'Unlock:').split('|')
          srr = []
          for v in cps:
            v = v.strip()
            vs = v.split()
            # print(len(vs), vs)
            if 'Unlock' in v:
              unlock = v.replace('Unlock:', '')
            if len(vs) == 1:
              continue
            else:
              srr.append("{}:{}".format(vs[0], vs[1]))
          craft = '|'.join(srr)
    elif len(hasImg) > 0:
        icons = hasImg[0]['style'].split(';')
        color = icons[0].split('/')[-1].split('.')[0]
        for tr in trs:
          th1 = tr.select('th')[0].get_text().strip()
          td1 = tr.select('td')[0]
          if 'rarity' in th1:
            rarity = td1.get_text().strip()
          if '技能' in th1:
            skill = td1.get_text('|').strip()
            skill = skill.replace('| Lv', ' Lv')
  charmArr.append([chmName, rarity, desc, skill, craft, unlock, preCharm, nextCharm, color])


names = []
with open(r'D:\git_me\script\python\charm\data\list.json', 'r', encoding='utf-8') as inf:
  list = json.loads(inf.readlines()[0])
  for arr in list:
    print('arr', arr)
    [name, url] = arr
    url = 'https://mhw.poedb.tw' + url
    chm = getItem(url, name)
    time.sleep(1)
  with open(r'D:\git_me\script\python\charm\data\t_charm0.sql', 'w', encoding='utf-8') as out:
    for chm in charmArr:
      [name, rarity, desc, skill, craft, unlock, pre, next, color] = chm
      if not name in names:
        names.append(name)
        print('chm', chm)
        sql = "insert into t_charm values (null, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', {})".format(name, rarity, desc, skill, craft, unlock, pre, next, color)
        out.write(sql+';\n')
  #   for line in sqls:
  #     out.write(line+';\n')

