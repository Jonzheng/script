import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_me\script\python\armor\data\list.html'
ff2 = r'D:\git_me\script\python\armor\data\list.json'

drr = []
crr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 1:
      td1 = tds[1]
      aa = td1.select('a')[0]
      link = aa['href']
      if link not in drr:
        drr.append(link)
        print(aa.string, link)
        crr.append([aa.string, link])
print(len(crr))

with open(ff2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr, ensure_ascii=False))