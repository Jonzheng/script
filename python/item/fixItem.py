Names = []
with open(r'D:\my_dev\script\python\item\data\t_items.txt', 'r', encoding='utf-8') as inf:
  for n in inf.readlines():
    n = n.strip()
    Names.append(n)

# luck = []

# with open(r'D:\my_dev\script\python\item\data\t_wp_craft.txt', 'r', encoding='utf-8') as inf:
#   for n in inf.readlines():
#     n = n.strip()
#     for sp in n.split('|'):
#       it = sp.split(':')[0]
#       if not it in Names and not it in luck:
#           luck.append(it)
# print(luck)
# luck = ['大痹贼龙的牙', '幻兽的雷尾', '银火龙的重壳', '樱火龙的重壳', '迅龙的厚鳞', '雷狼龙的刚爪', '雷狼龙的天玉', '炎王龙的刚角', '煌黑龙的凶爪', '黑轰龙的重牙', '爆锤龙的颚', '火龙的翼爪', '爆鳞龙的爆腺', '惨爪龙的强硬筋', '溟波龙的韧尾']


import sys
from bs4 import BeautifulSoup
import requests

host = 'https://mhw.poedb.tw'
mp = {'Investigation Reward (Purple)': '调查任务·紫', 'Investigation Reward (Gold)': '调查任务·金', 'Investigation Reward (Silver)':'调查任务·银','Investigation Reward (Bronze)':'调查任务·铜'}

sqls = []
def getItem(url, name='魂焰刚剑·灭尽'):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  desc = ''
  icon = ''
  rarity = 1
  carry = 1
  sell = 1
  buy = 1
  for cd in cards:
    head = cd.select('.card-header')
    ctext = cd.select('.card-text')
    tn = ''
    hasImg = []
    if head:
      tn = head[0].get_text().strip()
      hasImg = head[0].select('img')
    if ctext:
      desc = ctext[0].get_text().replace('\r', '').replace('\s', '').replace('\n', '').strip()
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if len(hasImg) > 0:
        icons = hasImg[0]['style'].split(';')
        icon = icons[1].split('/')[-1].split('.')[0] + '_' + icons[0].split('/')[-1].replace(')', '') # xx.png
        for tr in trs:
          th1 = tr.select('th')[0].get_text().strip()
          td1 = tr.select('td')[0].get_text().strip()
          if th1 == 'rarity':
            rarity = td1
          elif th1 == 'carry_limit':
            carry = td1
          elif th1 == '出售':
            sell = td1.replace('zenny', '')
          elif th1 == '购买':
            buy = td1.replace('zenny', '')
    elif 'Monster' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 5:
          [td1, td2, td3, td4, td5] = tds
          monName = td1.get_text().strip()
          cond = td2.get_text().strip()
          cond = cond.replace('Track', '怪物痕迹').replace('Shiny Drop', '掉落物').replace('Palico Bonus', '随从采集物')
          cond = cond.replace('The Guiding Lands', '引导之地').replace('Low', '低').replace('Mid', '中').replace('Tempered', '高')
          cond = cond.replace('%s的', monName).replace('%s', monName).replace('Investigation', '调查奖励')
          cond = cond.replace('Silver', '银').replace('Gold', '金').replace('Bronze', '铜').replace('Purple', '紫')
          cond = mp.get(cond, cond)
          rank = td3.get_text().strip()
          quantity = td4.get_text().replace('×', '').strip()
          percent = td5.get_text().replace('%', '').strip()
          sql2 = "insert into t_item_find (type, item_name, `rank`, `desc`, quantity, percent, monster_name) values(1,'{}','{}','{}',{},{},'{}');\n".format(name, rank, cond, quantity, percent, monName)
          sqls.append(sql2)
  return [desc, icon, rarity, carry, sell, buy]

with open(r'D:\my_dev\script\python\item\sql\t_in_items.sql', 'w', encoding='utf-8') as out1:
  with open(r'D:\my_dev\script\python\item\sql\t_up_find.sql', 'w', encoding='utf-8') as out2:
    with open(r'D:\my_dev\script\python\item\html\list.html', 'r', encoding='utf-8') as inf:
      tt = inf.read()
      soup = BeautifulSoup(tt, 'lxml')
      trs = soup.find_all(name='tr')
      for tr in trs:
        tds = tr.select('td')
        # print('ss', len(tds))
        if len(tds) == 2:
          [td1, td2] = tds[:2]
          al = td2.select('a')[0]
          name = al.get_text().strip()
          if not name in Names and not '？' in name and not '样本' in name:
            link = host + al['href']
            print(name, link)
            [desc, icon, rarity, carry, sell, buy] = getItem(link, name)
            sql = "insert into t_items (`cate`, `tag`, `name`, icon, `desc`, rarity, carry, buy, sell) values('material','reward','{}','{}','{}',{},{},{},{});\n".format(name, icon, desc, rarity, carry, buy, sell)
            out1.write(sql)
            for sql in sqls:
              out2.write(sql)
