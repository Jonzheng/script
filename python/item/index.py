import requests, json, time
from bs4 import BeautifulSoup

icons = []
type1 = []
type2 = []
with open(r'D:\git_pro\note\mhw\icons.json', 'r', encoding='utf-8') as inf:
   icons = json.loads(inf.read())
with open(r'D:\git_pro\note\mhw\type1.json', 'r', encoding='utf-8') as inf:
   type1 = json.loads(inf.read())
with open(r'D:\git_pro\note\mhw\type2.json', 'r', encoding='utf-8') as inf:
   type2 = json.loads(inf.read())

Names = []
with open(r'D:\git_pro\note\mhw\names2.txt', 'r', encoding='utf-8') as inf:
  for n in inf.readlines():
     n = n.strip()
     if n and not n in Names:
        Names.append(n)

print('icons:', len(icons), icons)
print('Name:', len(Names), Names[:9])

def getBasic(soup):
  title = soup.select('.project-title')[0]
  info = soup.select('.project-info')[0]
  desc1 = info.select('.col-sm-6')[0]
  tds = info.select('strong')
  img1 = title.select('img')[0]
  name1 = title.select('.align-self-center')[0]

  desc = desc1.get_text().strip()
  name = name1.get_text().replace('\'', '.').strip()
  if name in Names:
     name = '11111'
  img = img1['src']
  c1, c2, c3, c4 = tds
  rarity = c1.get_text().replace('稀有度', '').strip()
  carry = c2.get_text().replace('×', '').strip() # x×99
  buy = c3.get_text().replace('金', '').replace(',', '').strip()
  sell = c4.get_text().replace('金', '').replace(',', '').strip()

  img2 = requests.get(img)
  fna = img.split('/')[-1] # 22_8.png
  if not fna in icons:
    with open('D:/git_pro/note/mhw/icon/'+ fna, 'wb') as out:
      out.write(img2.content)
      icons.append(fna)
  sql = "insert into t_items (`cate`, `name`, icon, `desc`, rarity, carry, buy, sell) values('decora','{}','{}','{}',{},{},{},{});\n".format(name, fna, desc, rarity, carry, buy, sell)
  return sql, name

def getTable(soup, id):
  arr = []
  tables = soup.select('.table-lightborder')
  tb1, tb2, tb3, tb4 = tables
  mp = {'Investigation Reward (Purple)': '调查任务·紫', 'Investigation Reward (Gold)': '调查任务·金', 'Investigation Reward (Silver)':'调查任务·银','Investigation Reward (Bronze)':'调查任务·铜'}
  # 怪物狩猎
  trs = tb1.select('tr')
  arr = []
  for tr in trs:
    tds = tr.select('td')
    td1, td2, td3, td4, td5 = tds
    rank = td1.get_text().strip()
    monster_name = td2.get_text().strip()
    desc = td3.get_text().strip()
    desc = mp.get(desc, desc)
    quantity = td4.get_text().replace('×', '').strip()
    percent = td5.get_text().replace('%', '').strip()
    sql2 = "insert into t_item_find (type, item_name, `rank`, monster_name, `desc`, quantity, percent) values(1,'{}','{}','{}','{}',{},{});\n".format(id, rank, monster_name, desc, quantity, percent)
    arr.append(sql2)
  # 任务报酬
  trs = tb2.select('tr')
  for tr in trs:
    tds = tr.select('td')
    td1, td2, td3, td4 = tds
    quest_name = td1.select('a')[0].get_text().strip()
    quest_type = td1.select('img')[0]['src'].split('/')[-1]
    if not quest_type in type1:
       type1.append(quest_type)
    flg = quest_name[1:2]
    rank = '无位阶'
    if flg == '★':
        rank = '大师'
    elif int(flg) > 5:
        rank = '上位'
    else:
        rank = '下位'
    desc = td2.get_text().strip()
    quantity = td3.get_text().replace('×', '').strip()
    percent = td4.get_text().replace('%', '').strip()
    sql2 = "insert into t_item_find (type, item_name, `rank`, `desc`, quantity, percent, quest_name, quest_type) values(2,'{}','{}','{}',{},{},'{}','{}');\n".format(id, rank, desc, quantity, percent,quest_name, quest_type)
    arr.append(sql2)
  # 派遣随从
  trs = tb3.select('tr')
  for tr in trs:
    tds = tr.select('td')
    td1, td2, td3, td4, td5, td6, td7 = tds
    rank = td1.get_text().strip()
    stage = td2.get_text().strip()
    star = td3.get_text().strip()
    star = star.replace('&starf;', '★')
    quest_type = td4.select('img')[0]['src'].split('/')[-1]
    if not quest_type in type2:
       type2.append(quest_type)
    desc = td5.get_text().strip()
    desc = star + desc
    quantity = td6.get_text().replace('×', '').strip()
    percent = td7.get_text().replace('%', '').strip()
    sql2 = "insert into t_item_find (type, item_name, `rank`, `desc`, quantity, percent, quest_type) values(3,'{}','{}','{}',{},{},'{}');\n".format(id, rank, desc, quantity, percent, quest_type)
    arr.append(sql2)

  # 矿脉
  trs = tb4.select('tr')
  uniq = []
  for tr in trs:
    tds = tr.select('td')
    td1, td2, td3, td4, td5 = tds
    rank = td1.get_text().strip()
    stage = td2.get_text().strip()
    desc = td3.get_text().strip()
    kk = "{}{}{}".format(rank, stage, desc)
    if not desc or kk in uniq: continue
    uniq.append(kk)
    quantity = td4.get_text().replace('×', '').strip()
    percent = td5.get_text().replace('%', '').strip()
    sql2 = "insert into t_item_find (type, item_name, `rank`, stage, `desc`, quantity, percent) values(4,'{}','{}','{}','{}',{},{});\n".format(id, rank, stage, desc, quantity, percent)
    arr.append(sql2)
  return arr

idx = 0
with open(r'D:\git_pro\note\mhw\t_items_decora'+str(idx)+'.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\t_find_decora'+str(idx)+'.sql', 'w', encoding='utf-8') as out2:
    with open(r'D:\git_pro\note\mhw\link_decora.json', 'r', encoding='utf-8') as inf:
      dd = json.loads(inf.read())
      for it in dd[idx:]:
        print('=', it)
        if it[0] not in Names:
          resp = requests.get(it[1])
          soup = BeautifulSoup(resp.text, 'lxml')
          sql1, id = getBasic(soup)
          arr = getTable(soup, id)
          out.write(sql1)
          for ol in arr:
            out2.write(ol)
          time.sleep(1)

with open(r'D:\git_pro\note\mhw\icons.json', 'w', encoding='utf-8') as out:
    out.writelines(json.dumps(icons))
with open(r'D:\git_pro\note\mhw\type1.json', 'w', encoding='utf-8') as out:
    out.writelines(json.dumps(type1))
with open(r'D:\git_pro\note\mhw\type2.json', 'w', encoding='utf-8') as out:
    out.writelines(json.dumps(type2))

print('-end-', len(icons), len(type1), len(type2))