
import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_pro\note\mhw\decora.html'
ff2 = r'D:\git_pro\note\mhw\link_decora.json'

drr = []
crr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  arr = soup.find_all(name='a')
  for aa in arr:
    if aa.span:
      link = aa['href']
      if link not in drr:
        drr.append(link)
        print(aa.span.string, link, type(link))
        crr.append([aa.span.string, link])
print(len(crr))
print(crr[:3])

with open(ff2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr))