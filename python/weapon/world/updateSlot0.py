url = 'https://mhw.poedb.tw/chs/weapons/l_sword'
url = 'https://mhw.poedb.tw/chs/weapons/w_sword'
url = 'https://mhw.poedb.tw/chs/weapons/tachi'
url = 'https://mhw.poedb.tw/chs/weapons/sword'
url = 'https://mhw.poedb.tw/chs/weapons/c_axe'
url = 'https://mhw.poedb.tw/chs/weapons/hammer'
url = 'https://mhw.poedb.tw/chs/weapons/whistle'

# url = 'https://mhw.poedb.tw/chs/weapons/lance'
# url = 'https://mhw.poedb.tw/chs/weapons/g_lance'
# url = 'https://mhw.poedb.tw/chs/weapons/s_axe'
# url = 'https://mhw.poedb.tw/chs/weapons/rod'
# url = 'https://mhw.poedb.tw/chs/weapons/bow'
# url = 'https://mhw.poedb.tw/chs/weapons/lbg'
# url = 'https://mhw.poedb.tw/chs/weapons/hbg'
import requests
from bs4 import BeautifulSoup

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
tbs = soup.select('tbody')
with open(r'D:\git_me\script\python\weapon\sql\update_slot.sql', 'w', encoding='utf-8') as out:
  for tb in tbs:
    trs = tb.select('tr')
    tbrr = []
    for tr in trs:
      tdrr = []
      tds = tr.select('td')
      if len(tds) > 6:
        name = tds[0].get_text().strip()
        imgs = tds[5].select('img')
        arr = []
        if len(imgs) > 0 and '衍生' not in name:
          for img in imgs:
            slot = img['style'].split('/')[-1].split('.')[0]
            slot = slot.replace('66', '1').replace('67', '2').replace('68', '3').replace('72', '4')
            arr.append(slot)
          print(name, ','.join(arr))
          sql = "update t_weapon set slot = '{}' where name = '{}';\n".format(','.join(arr), name)
          out.write(sql)

