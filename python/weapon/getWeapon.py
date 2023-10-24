import time, json, requests, sys
from bs4 import BeautifulSoup
msql = []
HOST = 'https://mhw.poedb.tw'
def getItem(url):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  name = ''
  attack = 1
  lines = []
  for cd in cards:
    head = cd.select('.card-header')
    tn = ''
    if head:
      tn = head[0].get_text().strip()
    tb = cd.select('table')[0]

    print('@', tn)
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('th:', th)
    if '武器' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        # print('--line:', tds)
        [td1, td2, td3, td4, td5, td6] = tds[:6]
        name = td1.get_text().strip()
        link = HOST + td1.select('a')[0]['href']
        print(name)
        attack = td2.get_text().strip()
        element = td3.get_text().strip()
        afinity = td4.get_text().strip()
        defense = td5.get_text().strip()
        imgs = td6.select('img')
        slots = []
        for sl in imgs:
          slot = sl['style'].split('/')[-1].split('.')[0]
          slots.append(slot)
        # kbs = td7.select('.kbox-in')
        # print(name, element)
        # print('slots:', slots)
        # wrr = []
        # for kb in kbs:
        #   sps = kb.select('span')
        #   brr = []
        #   for sp in sps:
        #     brr.append([sp['class'][0].split('-')[-1], int(sp['title'])])
        #   wrr.append(brr)
        # wrr = [] ## 弓
        # sps = td7.select('span')
        # np = {'接': '接击瓶','強': '强击瓶','麻': '麻击瓶','毒': '毒瓶','睡': '睡眠瓶','爆': '爆破瓶'}
        # vp = {'green': '1', 'grey': '0'}
        # for sp in sps:
        #   brr = [np.get(sp.get_text().strip()), vp.get(sp['style'].split(':')[1].strip())]
        #   wrr.append(':'.join(brr))
        # print(wrr)
        one = [name, link, attack, afinity, defense, slots, '']
        lines.append(one)
    else:
      print('eeeee')
    print('='*88)
  return lines

# url = 'https://mhw.poedb.tw/chs/weapons/l_sword'
# url = 'https://mhw.poedb.tw/chs/weapons/w_sword'
# url = 'https://mhw.poedb.tw/chs/weapons/tachi'
# url = 'https://mhw.poedb.tw/chs/weapons/sword'
url = 'https://mhw.poedb.tw/chs/weapons/c_axe'
url = 'https://mhw.poedb.tw/chs/weapons/hammer'
url = 'https://mhw.poedb.tw/chs/weapons/whistle'
url = 'https://mhw.poedb.tw/chs/weapons/lance'
url = 'https://mhw.poedb.tw/chs/weapons/g_lance'
# url = 'https://mhw.poedb.tw/chs/weapons/s_axe'
# url = 'https://mhw.poedb.tw/chs/weapons/rod'
# url = 'https://mhw.poedb.tw/chs/weapons/bow'
# url = 'https://mhw.poedb.tw/chs/weapons/lbg'
# url = 'https://mhw.poedb.tw/chs/weapons/hbg'

with open(r'D:\git_pro\note\mhw\3_weapon\sql\246.json', 'w', encoding='utf-8') as out:
  lines = getItem(url)
  for ol in lines:
    out.write(json.dumps(ol, ensure_ascii=False) + '\n')
  time.sleep(1)