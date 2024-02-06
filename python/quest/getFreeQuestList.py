pre = 'https://mhw.poedb.tw/chs/quests/'

import requests, json, time
from bs4 import BeautifulSoup
from urllib.parse import unquote

drr = []
crr = []
for i in range(16):
  if i == 9:
    continue
  url = pre + str(i+1)
  print(url)
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  tb0 = soup.select('tbody')[0]
  trs = tb0.select('tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 3:
      [td1,td2,td3,td4] = tds
      rank = td1.get_text().strip()
      aa = td2.select('a')[0]
      link = aa['href']
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
        print(aa.string, link, rank, stage, icon, '|'.join(monEn))
        crr.append([aa.string, link, rank, stage, icon, '|'.join(monEn)])
    
  time.sleep(3)

with open(r'D:\git_me\script\python\quest\data\freeQuest.json', 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr, ensure_ascii=False))