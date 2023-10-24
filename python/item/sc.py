import requests, json
from bs4 import BeautifulSoup, element

fileOut1 = r'D:\git_pro\note\mhw\foo.html'
fileOut2 = r'D:\git_pro\note\mhw\ff123.json'

resp = requests.get('https://mhworld.kiranico.com/zh/items/rYm5r/bai-jiu-shi')
soup = BeautifulSoup(resp.text, 'lxml')

tableTag = soup.find_all(name='table')
# ht = soup.prettify()
# with open(fileOut1, 'w', encoding='utf-8') as f:
#   f.writelines(ts)
arr = []
idx = 0
for child in tableTag:
  # print('cc', list(child['class']), type(child['class']))
  if 'table-lightborder' in child['class']:
    idx += 1
    for tr in child.children:
      if tr.name == 'tbody':
        for line in tr.children:
          row = [idx]
          for td in line:
            if isinstance(td, element.Tag):
              if not td.a:
                cc = td.contents[0]
                if isinstance(cc, element.NavigableString):
                  row.append(cc.get_text().strip())
              else:
                url = td.a.img['src']
                tt = td.get_text().strip()
                row.append([url, tt])
              # if isinstance(cc, element.Tag):
              #   print('--cc', cc.a, type(cc.a))
                # row.append(cc.get_text().strip())
          if len(row) > 1:
            arr.append(row)

with open(fileOut2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(arr))
for it in arr:
  print('-', it)
print('-done-')