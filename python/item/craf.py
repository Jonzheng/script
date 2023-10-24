import requests
from bs4 import BeautifulSoup

resp = requests.get('https://mhworld.kiranico.com/zh/crafting')
soup = BeautifulSoup(resp.text, 'lxml')

tb = soup.select('.table-responsive')[0]

trs = tb.select('tr')

arr = []
for tr in trs:
    tds = tr.select('td')
    td1, td2, td3 = tds
    title = td1.get_text().strip()
    result = td1.select('a')[0].get_text().strip()
    quantity = 1
    if '×' in title:
        quantity = title.split('×')[1]
    td3a = td3.select('a')
    material2 = ''
    material1 = td3a[0].get_text().strip()
    if len(td3a) == 2:
        material2 = td3a[1].get_text().strip()
    sql2 = "insert into t_craft (result, quantity, kv1, kv2) values('{}',{},'{}','{}');\n".format(result, quantity, material1, material2)
    arr.append(sql2)

with open(r'D:\git_pro\note\mhw\craft0.sql', 'w', encoding='utf-8') as out:
  for line in arr:
      out.write(line)
