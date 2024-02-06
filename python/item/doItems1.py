
brr = []
import json
with open(r'D:\git_me\script\python\item\data\t_cloak.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    ss = ss.strip()
    if ss:
      [id, name, icon, color] = ss.split('\t')
      tag = 'cloak'
      icon = "{}-{}".format(icon, color)
      loc = 1
      brr.append([id, name, tag, icon, loc])

with open(r'D:\git_me\script\python\item\data\t_skill.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    ss = ss.strip()
    if ss:
      [id, name, icon, color] = ss.split('\t')
      tag = 'skill'
      icon = "{}-{}".format(icon, color)
      loc = 1
      brr.append([id, name, tag, icon, loc])

with open(r'D:\git_me\script\python\item\data\t_decor.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    ss = ss.strip()
    if ss:
      [id, name, icon, color] = ss.split('\t')
      tag = 'decor'
      icon = "{}-{}".format(icon, color)
      loc = 1
      brr.append([id, name, tag, icon, loc])

with open(r'D:\git_me\script\python\item\data\t_items1.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    ss = ss.strip()
    [id, name, tag, icon] = ss.split('\t')
    icon = icon.split('.')[0]
    tag = 'item'
    brr.append([id, name, tag, icon])

with open(r'D:\git_me\script\python\item\data\items1.js', 'w', encoding='utf-8') as out:
  out.write(json.dumps(brr, ensure_ascii=False))
