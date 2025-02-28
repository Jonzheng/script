import requests, json, time
from bs4 import BeautifulSoup, element

tag = '结算道具'
link = 'https://gamecat.fun/rise/zh/index.php?title=' + tag + '/'
def getItemList():
  with open(r'D:\pro\script\python\item\html\item9.html', 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    items = []
    for tr in trs:
      tds = tr.select('td')
      # print('ss', len(tds))
      if len(tds) == 4:
        [td1, td2, td3, td4] = tds[:4]
        al = td2.select('a')[0]
        name = al.get_text().strip()
        en_jp = td3.get_text().strip()
        [en, jp] = en_jp.split('/')
        desc = td4.get_text().strip()
        en = en.strip()
        jp = jp.strip()
        items.append([name, en, jp, desc])
    return items

def scraftItem(link):
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
  zrr = []
  for tb in tableTag:
    th = tb.select('th')
    if len(th) > 0:
      thh = th[0].get_text().replace('\r', '').replace('\n', '').strip()
      for tbd in tb.select('tbody'):
        idx += 1
        print('___idx', idx, thh)
        if '分类' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 4:
              [td1, td2, td3, td4] = tds
              tag = td1.get_text().replace('\r', '').replace('\n', '').strip()
              rare = td2.get_text().replace('\r', '').replace('\n', '').strip()
              buy = td3.get_text().replace('\r', '').replace('\n', '').strip()
              sale = td4.get_text().replace('\r', '').replace('\n', '').strip()
              # print('__tag', tag, rare, 'B', buy, sale)
              base = [tag, rare, buy, sale]
        elif '中文简体' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 4:
              [td1, td2, td3, td4] = tds
              # name = td1.get_text().replace('\r', '').replace('\n', '').strip()
              hk = td2.get_text().replace('\r', '').replace('\n', '').strip()
              en = td3.get_text().replace('\r', '').replace('\n', '').strip()
              jp = td4.get_text().replace('\r', '').replace('\n', '').strip()
              zrr = [hk, en, jp]
              print('_hk', zrr)
        elif '怪物' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            # print(idx, len(tds))
            if len(tds) == 5:
              [td1, td2, td3, td4, td5] = tds
              mon = td1.get_text().replace('\r', '').replace('\n', '').strip()
              rank = td2.get_text().replace('\r', '').replace('\n', '').strip()
              desc = td3.get_text().replace('\r', '').replace('\n', '').strip()
              quan = td4.get_text().replace('\r', '').replace('\n', '').strip()
              perc = td5.get_text().replace('\r', '').replace('\n', '').strip()
              # print('__mon', mon, rank, 'B', desc, quan, perc)
              finds.append([mon, rank, desc, quan, perc])
        elif '商店购买' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            if len(tds) == 5:
              for td in tds:
                w1 = td.get_text().replace('\r', '').replace('\n', '').strip()
                ways.append(w1)
        elif '原料1' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            # print(idx, len(tds))
            if len(tds) == 4:
              [td1, td2, td3, td4] = tds
              kv1 = td1.get_text().replace('\r', '').replace('\n', '').strip()
              kv2 = td2.get_text().replace('\r', '').replace('\n', '').strip()
              result = td3.get_text().replace('\r', '').replace('\n', '').strip()
              quan = td4.get_text().replace('\r', '').replace('\n', '').strip()
              crafts.append([kv1, kv2, result, quan])
        elif '衍生方式' in thh:
          for tr in tbd.select('tr'):
            tds = tr.select('td')
            # print(idx, len(tds))
            if len(tds) == 6:
              [td1, td2, td3, td4, td5, td6] = tds
              quest_type = td1.get_text().replace('\r', '').replace('\n', '').strip()
              star = td2.get_text().replace('\r', '').replace('\n', '').strip()
              quest_name = td3.get_text().replace('\r', '').replace('\n', '').strip()
              desc = td4.get_text().replace('\r', '').replace('\n', '').strip()
              quan = td5.get_text().replace('\r', '').replace('\n', '').strip()
              perc = td6.get_text().replace('\r', '').replace('\n', '').strip()
              # print('__que', quest_type, star, 'D', quest_name, desc, quan, perc)
              ques.append([quest_type, star, quest_name, desc, quan, perc])
  return [base, finds, ques,zrr, crafts, '|'.join(ways)]

items = getItemList()
with open(r'D:\pro\script\python\item\data\r_item9.txt', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\item\data\r_item_find9.txt', 'w', encoding='utf-8') as out2:
    with open(r'D:\pro\script\python\item\data\r_craft9.txt', 'w', encoding='utf-8') as out3:
      for irr in items:
        [name, en, jp, desc] = irr
        name = name.replace(' ', '').strip()
        [base, finds, ques, zrr, crafts, way] = scraftItem(link+name)
        [tag, rare, buy, sale] = base
        [hk, en, jp] = zrr
        line1 = '\t'.join([name, tag, rare, hk, en, jp, buy, sale, desc, way])
        out.write(line1+'\n')
        for find in finds:
          [mon, rank, desc, quan, perc] = find
          line1 = '\t'.join([name, '1', mon, rank, desc, quan, perc])
          out2.write(line1+'\n')
        for find in ques:
          [quest_type, star, quest_name, desc, quan, perc] = find
          line1 = '\t'.join([name, '2', quest_type, star, quest_name, desc, quan, perc])
          out2.write(line1+'\n')
        for crf in crafts:
          line1 = '\t'.join(crf)
          out3.write(line1+'\n')
        time.sleep(1)