from bs4 import BeautifulSoup

ff1 = r'D:\git_me\script\python\decor\list.html'
ff2 = r'D:\git_me\script\python\decor\t_decor.sql'

sqls = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 4:
      [td1, td2, td3, td4, td5] = tds
      sty = td1.select('img')[0]['style']
      icon = sty.split('/')[-1].split('.')[0]
      icon = int(icon) + 1
      color = sty.split(';')[0].split('/')[-1].split('.')[0]
      name = td2.get_text().strip()
      rarity = td3.get_text().strip()
      slots = td4.get_text().strip()
      skill = td5.get_text("|").strip()
      skill = skill.replace('| Lv ', ':').replace('すりんがーそうてんすうあっぷ', '投射器装填数提升')
      print(icon, color, name, rarity, slots)
      print('=', skill)
      sql = "insert into t_decor values (null, '{}', '{}', {}, {}, {}, {})".format(name,skill, rarity, slots, icon, color)
      sqls.append(sql)

with open(ff2, 'w', encoding='utf-8') as out:
  for sql in sqls:
    out.write(sql+';\n')