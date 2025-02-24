import requests, json, time
from bs4 import BeautifulSoup, element
host = 'https://gamecat.fun'
tag = '结算道具'
link = 'https://gamecat.fun/rise/zh/index.php?title=' + tag + '/'
def getItemList():
  with open(r'D:\pro\script\python\weapon\html\242.html', 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    items = []
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 9:
        for td in tds:
          arr = td.select('a')
          if len(arr) > 1:
            wp = arr[0].get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
            if wp:
              suf = arr[0]['href']# 械・大
              print('__', wp, suf)

    return items

def scraftItem(name):
  link = 'https://gamecat.fun/rise/zh/index.php?title=武器/大剑/' + name
  resp = requests.get(link)
  soup = BeautifulSoup(resp.text, 'lxml')
  tableTag = soup.find_all(name='table')
  print(link)
  idx = 0
  base = []
  finds = []
  ques = []
  crafts = []
  ways = []
  for tb in tableTag:
    th = tb.select('th')
    if len(th) > 0:
      thh = th[0].get_text().replace('\r', '').replace('\n', '').strip()
      for tbd in tb.select('tbody'):
        idx += 1
        print('___idx', idx, thh)
        if name == thh:
          trs = tbd.select('tr')
          tds = trs[1].select('td')
          if len(tds) > 0:
            img = tds[0].select('a img')
            print('__', img[0]['src'])
        elif '中文简体' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 4:
              [td1, td2, td3, td4] = tds
              name = td1.get_text().replace('\r', '').replace('\n', '').strip()
              hk = td2.get_text().replace('\r', '').replace('\n', '').strip()
              en = td3.get_text().replace('\r', '').replace('\n', '').strip()
              jp = td4.get_text().replace('\r', '').replace('\n', '').strip()
              base = [hk, en, jp]
              print('__base', base)
        elif '饰品槽' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 2:
              [td1, td2] = tds
              ta1 = td1.select('a')
              ta2 = td2.select('a')
              a1 = []
              a2 = []
              for ta in ta1:
                st = ta['title'].replace('-star', '').replace('no', '').strip()
                if st:
                  a1.append(st)
              for ta in ta2:
                st = ta['title'].replace('-star', '').replace('no', '').strip()
                if st:
                  a2.append(st)
              print('__slot', a1, a2)
        elif '衍生方式' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 7:
              [td1, td2, td3, td4, td5, td6, td7] = tds
              d1 = td1.get_text().replace('\r', '').replace('\n', '').strip()
              d2 = td2.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip()
              d5 = td5.get_text().replace('\r', '').replace('\n', '').strip()
              d6 = td6.select('p')
              d7 = td7.select('p')
              print('__d1', d1)
              print('__d2', d2)
              print('__d5', d5)
              if len(d6) > 0:
                for p in d6:
                  print('____p6', p.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip())
              if len(d7) > 0:
                for p in d7:
                  print('____p7', p.get_text().replace('\r', '').replace('\n', '').replace(' ', '').strip())
            elif len(tds) == 6:
              [td1, td2, td3, td4, td5, td6] = tds
              d2 = td2.get_text().replace('\r', '').replace('\n', '').strip()
              print('_____next', d2)
# items = getItemList()
# with open(r'D:\pro\script\python\weapon\data\r_item242.txt', 'w', encoding='utf-8') as out:
#   with open(r'D:\pro\script\python\weapon\data\r_item_find242.txt', 'w', encoding='utf-8') as out2:
#     with open(r'D:\pro\script\python\weapon\data\r_craft242.txt', 'w', encoding='utf-8') as out3:
#       for irr in items:
#         [name, en, jp, desc] = irr
#         name = name.replace(' ', '').strip()
#         [base, finds, ques, crafts, way] = scraftItem(link+name)
#         [tag, rare, buy, sale] = base
#         line1 = '\t'.join([name,tag, rare, buy, sale, en, jp, desc, way])
#         out.write(line1+'\n')
#         for find in finds:
#           [mon, rank, desc, quan, perc] = find
#           line1 = '\t'.join([name, '1', mon, rank, desc, quan, perc])
#           out2.write(line1+'\n')
#         for find in ques:
#           [quest_type, star, quest_name, desc, quan, perc] = find
#           line1 = '\t'.join([name, '2', quest_type, star, quest_name, desc, quan, perc])
#           out2.write(line1+'\n')
#         for crf in crafts:
#           line1 = '\t'.join(crf)
#           out3.write(line1+'\n')
#         time.sleep(1)

scraftItem('茜霞紫微两断剑')
