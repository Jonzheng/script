import time, json, requests, sys
from bs4 import BeautifulSoup, element

def getItem(link):
  print('link:', link)
  drr = link.split('/')
  resp = requests.get(link)
  soup = BeautifulSoup(resp.text, 'lxml')
  tableTag = soup.find_all(name='table')
  arr = []
  idx = 0
  for child in tableTag:
    if 'table-lightborder' in child['class']:
      idx += 1
      for tr in child.children:
        if tr.name == 'tbody':
          for line in tr.children:
            row = [idx]
            for td in line:
              if isinstance(td, element.Tag):
                if not td.a:
                  # print('nota', type(td), td)
                  row.append(td.get_text().strip())
                else:
                  url = td.a.img['src']
                  tt = td.get_text().strip()
                  row.append([url, tt])
            if len(row) > 1:
              arr.append(row)
  return arr, drr[-2], drr[-1]

def outJson(arr, key, name):
  print('out:', key, name)
  ff = "D:/git_pro/note/mhw/" + name + ".json"
  with open(ff, 'w', encoding='utf-8') as out:
    out.writelines(json.dumps(arr))

links = r'D:\git_pro\note\mhw\links.json'
count = 0
with open(links, 'r', encoding='utf-8') as inf:
    dd = json.loads(inf.read())
    for line in dd:
        count += 1
        arr, key, name = getItem(line[1])
        outJson(arr, key, name)
        if count % 3 == 0:
          time.sleep(1)
          sys.exit()
        # if count % 60 == 0:
        #     time.sleep(2)

