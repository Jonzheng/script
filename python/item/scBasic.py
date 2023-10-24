import requests
from bs4 import BeautifulSoup

resp = requests.get('https://mhworld.kiranico.com/zh/items/oVA5e/kuang-ben-cui-qu-ye')
soup = BeautifulSoup(resp.text, 'lxml')

title = soup.select('.project-title')[0]
info = soup.select('.project-info')[0]
desc1 = info.select('.col-sm-6')[0]

tds = info.select('strong')

img1 = title.select('img')[0]
name1 = title.select('.align-self-center')[0]

desc = desc1.get_text().strip()
name = name1.get_text().strip()
img = img1['src']

print(name)
print(desc)
print(img)

c1, c2, c3, c4 = tds

rarity = c1.get_text().replace('稀有度', '').strip()
carry = c2.get_text().replace('×', '').strip() # x×99
buy = c3.get_text().replace('金', '').replace(',', '').strip()
sell = c4.get_text().replace('金', '').replace(',', '').strip()

img2 = requests.get(img)
fna = img.split('/')[-1] # 22_8.png
sp1 = fna.split('.')[0].split('_')
id = int(sp1[0]) * 10000 + int(sp1[1])
print(type(img2.content))
with open('D:/git_pro/note/mhw/icon/'+ fna, 'wb') as out:
    out.write(img2.content)

sql1 = "insert into t_material (id, `name`, icon, `desc`, rarity, carry, buy, sell) values({},'{}','{}','{}',{},{},{},{});\n".format(id, name, fna, desc, rarity, carry, buy, sell)

count = 0
tables = soup.select('.table-lightborder')
tb1, tb2, tb3, tb4 = tables

mp = {'Investigation Reward (Gold)': '调查任务·金', 'Investigation Reward (Silver)':'调查任务·银','Investigation Reward (Bronze)':'调查任务·铜'}
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
    sql2 = "insert into t_item_find (type, item_name, `rank`, monster_name, `desc`, quantity, percent) values(1,'{}','{}','{}','{}',{},{});\n".format(name, rank, monster_name, desc, quantity, percent)
    arr.append(sql2)
# 任务报酬
trs = tb2.select('tr')
for tr in trs:
    tds = tr.select('td')
    td1, td2, td3, td4 = tds
    quest_name = td1.select('a')[0].get_text().strip()
    quest_type = td1.select('img')[0]['src'].split('/')[-1]
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
    sql2 = "insert into t_item_find (type, item_name, `rank`, `desc`, quantity, percent, quest_name, quest_type) values(2,'{}','{}','{}',{},{},'{}','{}');\n".format(name, rank, desc, quantity, percent,quest_name, quest_type)
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
    desc = star + td5.get_text().strip()
    quantity = td6.get_text().replace('×', '').strip()
    percent = td7.get_text().replace('%', '').strip()
    sql2 = "insert into t_item_find (type, item_name, `rank`, `desc`, quantity, percent, quest_type) values(3,'{}','{}','{}',{},{},'{}');\n".format(name, rank, desc, quantity, percent, quest_type)
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
    sql2 = "insert into t_item_find (type, item_name, `rank`, stage, `desc`, quantity, percent) values(4,{},'{}','{}','{}',{},{});\n".format(name, rank, stage, desc, quantity, percent)
    arr.append(sql2)

with open(r'D:\git_pro\note\mhw\foo.sql', 'w', encoding='utf-8') as out:
  for line in arr:
      out.write(line)

print('-done-')