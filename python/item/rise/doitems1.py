import json
brr = []
with open(r'D:\pro\script\python\item\data\r_items1.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    ss = ss.strip()
    [id, name, tag, icon, hk] = ss.split('\t')
    icon = icon.split('.')[0]
    brr.append([id, name, tag, icon, hk])

with open(r'D:\pro\script\python\item\data\riseItems1.js', 'w', encoding='utf-8') as out:
  out.write(json.dumps(brr, ensure_ascii=False))