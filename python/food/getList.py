import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_me\script\python\food\table.html'
ff2 = r'D:\git_me\script\python\food\list.sql'
ff3 = r'D:\git_me\script\python\food\t_quest.txt'

qm = {}
with open(ff3, 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    [id, name] = line.strip().split('\t')
    qm[name] = id
  
print(qm)

with open(ff2, 'w', encoding='utf-8') as out:
  with open(ff1, 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 2:
        [td1, td2, td3] = tds
        sty = td1.select('img')[0]['style']
        icon = sty.split('/')[-1].split('.')[0]
        icon = int(icon) + 1
        color = sty.split(';')[0].split('/')[-1].split('.')[0]
        name = td1.get_text().strip()
        desc = td2.get_text().replace('\n', '').replace('《', '').replace('》', '').replace('[', '').replace(']', '').strip()
        ds = desc.split('  ')
        type = ds[0].replace('食材，容易发动', '').replace('，容易发动', '')
        effect = ds[1].replace('体系料理技能。', '').replace('系用餐技能。', '')
        desc = ds[2]
        unlock = td3.get_text().strip()
        qid = qm.get(unlock, 0)
        sql = "insert into t_food values (null, {}, {}, '{}', '{}', '{}', '{}', {}, '{}');".format(icon, color, name, type, effect, desc, qid, unlock)
        out.write(sql + '\n')


