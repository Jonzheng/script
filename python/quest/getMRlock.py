import re
from bs4 import BeautifulSoup

ff1 = r'D:\git_me\script\python\quest\mrlist.html'
ff2 = r'D:\git_me\script\python\quest\data\qunlockMR.txt'

arr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  tbs = soup.find_all(name='table')
  for tb in tbs:
    trs = tb.find_all(name='tr')
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 2:
        [td1,td2,td3] = tds
        aa = td1.select('a')[0]
        qname = aa.get_text().replace('\'', '·').strip()
        condit = td3.get_text('|').replace('\r', '').replace('\n', '').strip()
        condit = re.sub(' +', ' ', condit)
        condit = condit.split('|')[-1].replace(':', '').replace('”', '\"').replace('\'', '·').strip()
        print(qname)
        print(condit)
        print('-'*88)
        arr.append([qname, condit])

with open(ff2, 'a', encoding='utf-8') as out:
  for brr in arr:
    out.write('\t||\t'.join(brr)+'\n')