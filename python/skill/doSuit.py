
mp = {}
dp = {}
with open(r'D:\git_me\script\python\skill\data\suit.txt', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    [id, name, desc] = ss.strip().split('\t')
    suitArr = []
    id = int(id)
    dp[name] = {'id': id, 'val': name}
    mp[id] = {'suitId': id, 'suitName': name}
    for sks in desc.split('|'):
      [lv, sk, dd] = sks.split(';')
      skName = sk.split(':')[0]
      print(name, skName, lv)
      suitArr.append({'lv':int(lv), 'skName': skName})
    mp[id]['suitArr'] = suitArr
print(dp)

arr = []
for nn in ['冰呪龙的神秘','溟波龙的神秘','天地煌啼龙的神秘','太古的神秘','幻兽的神秘','金火龙的真髓','银火龙的真髓','雌火龙的真髓','火龙的真髓','迅龙的真髓','斩龙的真髓','碎龙的真髓','轰龙的真髓','恐暴龙的真髓','熔山龙的真髓','炎妃龙的真髓','雷狼龙的真髓','角龙的霸气','爆锤龙的霸气','爆鳞龙的霸气','蛮颚龙的霸气','灭尽龙的霸气','金狮子的怒气','调查团的炼金术','钢龙之飞翔','炎王龙之武技','冰牙龙的秘技','尸套龙的灵脉']:
  arr.append(dp[nn])

print(arr)