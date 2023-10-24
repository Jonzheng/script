import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_pro\note\mhw\0_monsters\mon_link2.html'
ff2 = r'D:\git_pro\note\mhw\0_monsters\mon_link2.json'

drr = []
crr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  arr = soup.find_all(name='a')
  for aa in arr:
    link = aa['href']
    if link not in drr:
      drr.append(link)
      print(aa.string, link)
      crr.append([aa.string, link])
print(len(crr))

with open(ff2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr, ensure_ascii=False))