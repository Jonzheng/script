import json

# with open(r'D:\git_me\script\python\quest\data\hEvent.txt', 'r', encoding='utf-8') as inf:
#   with open(r'D:\git_me\script\python\quest\data\mEvent.txt', 'r', encoding='utf-8') as inf:
#     with open(r'D:\git_me\script\python\quest\data\Assigned.txt', 'r', encoding='utf-8') as inf:
mp = {}
with open(r'D:\git_me\script\python\quest\data\Assigned.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip().strip(';')
    dd = json.loads(line)
    name = dd[2]
    nameEn = dd[-2].lower().strip()
    print(name, nameEn)
    mp[nameEn] = name

with open(r'D:\git_me\script\python\quest\data\freeQuest.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip().strip(';')
    dd = json.loads(line)
    name = dd[2]
    nameEn = dd[-2].lower().strip()
    print(name, nameEn)
    mp[nameEn] = name
mon = {}
with open(r'D:\git_me\script\python\monster\data\t_monster.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip()
    [name, nameEn] = line.split('\t')
    mon[nameEn] = name
print('-'*99)
def getCd(en):
  arr = en.split('\"')
  cc = 0
  for na in arr:
    zh = mp.get(na.lower().strip())
    if cc % 2 == 1 and zh:
      en = en.replace(na, zh)
    cc += 1
  for kk in mon:
    if kk in en:
      en = en.replace(kk, mon.get(kk))
  en = en.replace('Complete the quest ', '完成')
  en = en.replace('Clear the optional quests ', '完成')
  en = en.replace('Complete the Mission ', '完成')
  en = en.replace('clearing the assigned quest ', '完成')
  en = en.replace('Complete the Mission ', '完成')
  en = en.replace('Complete the assigned quest ', '完成')
  en = en.replace('Clear the quest ', '完成')
  en = en.replace('Complete the optional quests ', '完成')
  en = en.replace('Clear ', '完成')
  en = en.replace('master rank', '大师')
  en = en.replace('capture a', '捕获')
  en = en.replace('captured a', '捕获')
  en = en.replace('Hunt a ', '狩猎')
  en = en.replace('discovering a', '发现')
  en = en.replace('discover a', '发现')
  en = en.replace('Discover a', '发现')
  en = en.replace('discovered a', '发现')
  en = en.replace('Discover', '发现')
  en = en.replace('Seliana', '月辰')
  en = en.replace('Astera', '星辰')
  en = en.replace('Hoarfrost Reach', '永霜冻土')
  en = en.replace('tigrex', '轰龙')
  en = en.replace('botanist', '温和的植物学者')
  en = en.replace('high rank', '上位')
  en = en.replace('the chef', '料理长')
  en = en.replace(' and 捕获', '和捕获')
  en = en.replace('捕获n', '捕获')
  en = en.replace('Coral Highlands', '珊瑚高地')
  en = en.replace('armor shop attendant', '武器店')
  en = en.replace('Elder·s Recess', '龙结晶之地')
  en = en.replace('·s Smithy', '武器店')
  en = en.replace('Armory NPC', '武器店')
  en = en.replace('Jovial Scholar', '乐观的学者')
  en = en.replace('No Remorse, No Surrender', '潘多拉的斗技场')
  en = en.replace('He Taketh It With His eyes', '受伤的魔兽贝希摩斯')
  en = en.replace('Confluence of Fates', '收束之地')
  return en.strip('.')

with open(r'D:\git_me\script\python\quest\data\unlockDataHR.txt', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\quest\data\qunlockHR.txt', 'r', encoding='utf-8') as inf:
    for line in inf.readlines():
      line = line.strip()
      [en, cd] = line.split('	||	')
      en = en.lower().strip()
      if (mp.get(en)):
        print(mp.get(en), getCd(cd))
        out.write(mp.get(en) + '\t' + getCd(cd) + '\n')
      else:
        print('---', en)
      

