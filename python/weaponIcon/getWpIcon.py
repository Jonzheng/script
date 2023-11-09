
import requests, time
from bs4 import BeautifulSoup

ff0 = r'D:\my_dev\script\python\weapon\t_weapon.txt'
ff1 = r'D:\my_dev\script\python\weaponIcon\html\254.html'

drr = []
crr = []
np = {}
with open(ff0, 'r', encoding='utf-8') as inf:
  for il in inf.readlines():
    sprr = il.strip().split('\t')
    if len(sprr) == 3:
      [id, name, type] = sprr
      np[name] = '{}.png'.format(id)

with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    # print('ss', len(tds))
    if len(tds) == 5:
      [td1, td2, td3, td4, td5] = tds[:5]
      name = td1.select('a')[0].get_text().strip()
      img = td1.select('img')[0]
      src = img['src']
      print(name, src)
      resp = requests.get(src)
      if resp.status_code == 200:
        fna = np.get(name)
        if fna:
          with open('D:/my_dev/script/python/weaponIcon/out/254/'+ fna, 'wb') as out:
            out.write(resp.content)
        else:
          print('not', name)
      # time.sleep(1)
