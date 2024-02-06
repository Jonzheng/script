import json
from bs4 import BeautifulSoup
from urllib.parse import unquote

ff1 = r'D:\git_me\script\python\quest\data\assigned.html'
ff1 = r'D:\git_me\script\python\quest\data\eventQuest.html'
ff1 = r'D:\git_me\script\python\quest\data\mEvent.html'
ff1 = r'D:\git_me\script\python\quest\data\Assignments.html'
ff1 = r'D:\git_me\script\python\quest\data\Challenges.html'
ff1 = r'D:\git_me\script\python\quest\data\Arena.html'
ff2 = r'D:\git_me\script\python\quest\data\Arena.json'

drr = []
crr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 3:
      [td1,td2,td3,td4] = tds
      rank = td1.get_text().strip()
      aa = td2.select('a')[0]
      link = aa['href']
      print(td3)
      a3s = td3.select('a')
      monEn = []
      for a3 in a3s:
        m = unquote(a3['href'].split('/')[-1]).replace('\'', '·')
        monEn.append(m)
      img = td2.select('img')[0]
      icon = int(img['src'].split('/')[-1].split('.')[0]) + 1
      stage = td4.get_text().strip()
      if link not in drr:
        drr.append(link)
        print(rank, stage, icon, aa.string, link)
        crr.append([aa.string, link, rank, stage, icon, '|'.join(monEn)])
print(len(crr))

with open(ff2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr, ensure_ascii=False))