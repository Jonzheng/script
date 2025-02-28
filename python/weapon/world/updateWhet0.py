# url = 'https://mhw.poedb.tw/chs/weapons/l_sword'
# url = 'https://mhw.poedb.tw/chs/weapons/w_sword'
# url = 'https://mhw.poedb.tw/chs/weapons/tachi'
# url = 'https://mhw.poedb.tw/chs/weapons/sword'
# url = 'https://mhw.poedb.tw/chs/weapons/c_axe'
# url = 'https://mhw.poedb.tw/chs/weapons/hammer'
# url = 'https://mhw.poedb.tw/chs/weapons/whistle'

url = 'https://mhw.poedb.tw/chs/weapons/lance'
url = 'https://mhw.poedb.tw/chs/weapons/g_lance'
url = 'https://mhw.poedb.tw/chs/weapons/s_axe'
url = 'https://mhw.poedb.tw/chs/weapons/rod'
url = 'https://mhw.poedb.tw/chs/weapons/bow'
# url = 'https://mhw.poedb.tw/chs/weapons/lbg'
# url = 'https://mhw.poedb.tw/chs/weapons/hbg'
import requests
from bs4 import BeautifulSoup
from functools import reduce

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
tbs = soup.select('tbody')
with open(r'D:\git_me\script\python\weapon\sql\update_whet0.sql', 'w', encoding='utf-8') as out:
  for tb in tbs:
    trs = tb.select('tr')
    tbrr = []
    for tr in trs:
      tdrr = []
      tds = tr.select('td')
      if len(tds) > 6:
        name = tds[0].get_text().strip()
        box = tds[6].select('.kbox-in')
        arr = []
        if len(box) > 1:
          [b1, b2] = box
          a1 = b1.select('.bg-danger')[0]['title'] if b1.select('.bg-danger') else '0'
          a2 = b1.select('.bg-warning')[0]['title'] if b1.select('.bg-warning') else '0'
          a3 = b1.select('.bg-yellow')[0]['title'] if b1.select('.bg-yellow') else '0'
          a4 = b1.select('.bg-success')[0]['title'] if b1.select('.bg-success') else '0'
          a5 = b1.select('.bg-blue')[0]['title'] if b1.select('.bg-blue') else '0'
          a6 = b1.select('.bg-white')[0]['title'] if b1.select('.bg-white') else '0'
          a7 = b1.select('.bg-purple')[0]['title'] if b1.select('.bg-purple') else '0'
          # a8 = b1.select('.bg-dark')[0]['title'] if b1.select('.bg-dark') else '0'

          c1 = b2.select('.bg-danger')[0]['title'] if b2.select('.bg-danger') else '0'
          c2 = b2.select('.bg-warning')[0]['title'] if b2.select('.bg-warning') else '0'
          c3 = b2.select('.bg-yellow')[0]['title'] if b2.select('.bg-yellow') else '0'
          c4 = b2.select('.bg-success')[0]['title'] if b2.select('.bg-success') else '0'
          c5 = b2.select('.bg-blue')[0]['title'] if b2.select('.bg-blue') else '0'
          c6 = b2.select('.bg-white')[0]['title'] if b2.select('.bg-white') else '0'
          c7 = b2.select('.bg-purple')[0]['title'] if b2.select('.bg-purple') else '0'
          # c8 = b2.select('.bg-dark')[0]['title'] if b2.select('.bg-dark') else '0'

          arr = [a1, a2, a3,a4,a5,a6,a7]
          brr = [c1, c2, c3,c4,c5,c6,c7]
          sum1 = reduce(lambda x, y: int(x)+int(y), arr)
          sum2 = reduce(lambda x, y: int(x)+int(y), brr)
          whet = ','.join(arr)+'|'+','.join(brr)
          print(name,sum1,sum2, whet)
          sql = "update t_weapon set whet = '{}' where name = '{}';\n".format(whet, name)
          out.write(sql)

