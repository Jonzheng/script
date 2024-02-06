import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_me\script\python\lands\data\table.html'
ff2 = r'D:\git_me\script\python\lands\data\table.sql'

sqls = []
uni = {}
arr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 9:
      [td1, td2, td3, td4, td5, td6, td7, td8, td9, td10] = tds
      stage = td1.get_text().replace('古代树森林', '森林地带').strip()
      stage = stage.replace('大蚁冢荒地', '荒地地带').replace('陆珊瑚台地', '陆珊瑚地带')
      stage = stage.replace('瘴气之谷', '瘴气地带').replace('龙结晶之地', '熔岩地带').replace('永霜冻土', '冰雪地带')
      monName = td3.get_text().strip()
      lv1 = td4.get_text().split('(')[0].strip()
      if lv1:
        tp = '1' if 'bg-tempered' in td4['class'] else '0'
        lv1 += '|' + tp
      lv2 = td5.get_text().split('(')[0].strip()
      if lv2:
        tp = '1' if 'bg-tempered' in td5['class'] else '0'
        lv2 += '|' + tp
      lv3 = td6.get_text().split('(')[0].strip()
      if lv3:
        tp = '1' if 'bg-tempered' in td6['class'] else '0'
        lv3 += '|' + tp
      lv4 = td7.get_text().split('(')[0].strip()
      if lv4:
        tp = '1' if 'bg-tempered' in td7['class'] else '0'
        lv4 += '|' + tp
      lv5 = td8.get_text().split('(')[0].strip()
      if lv5:
        tp = '1' if 'bg-tempered' in td8['class'] else '0'
        lv5 += '|' + tp
      lv6 = td9.get_text().split('(')[0].strip()
      if lv6:
        tp = '1' if 'bg-tempered' in td9['class'] else '0'
        lv6 += '|' + tp
      lv7 = td10.get_text().split('(')[0].strip()
      if lv7:
        tp = '1' if 'bg-tempered' in td10['class'] else '0'
        lv7 += '|' + tp
      if uni.get(monName):
        uni[monName].append(stage)
      else:
        uni[monName] = [stage]
      # arr.append([stage, monName, lv1, lv2, lv3, lv4, lv5, lv6, lv7])
      print(stage, monName, lv1, lv2, lv3, lv4, lv5, lv6, lv7)
      sql = "insert into t_land_monster values (null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(stage, monName, lv1, lv2, lv3, lv4, lv5, lv6, lv7)
      sqls.append(sql)


# with open(ff2, 'w', encoding='utf-8') as out:
#   for line in sqls:
#     out.write(line+';\n')

un = []

# ['大贼龙', '飞雷龙', '黑狼鸟', '战痕黑狼鸟', '搔鸟', '土砂龙', '角龙', '黑角龙', '眩鸟', '浮空龙', '水妖鸟', '麒麟', '溟波龙', '大痹贼龙', '骨锤龙', '硫斩龙', '雾瘴尸套龙', '黑轰龙', '岩贼龙', '熔岩龙', '爆锤龙', '碎龙', '红莲爆鳞龙', '痹毒龙', '冰牙龙', '霜翼风漂龙', '狱狼龙']
# 大贼龙|飞雷龙|黑狼鸟|战痕黑狼鸟|搔鸟|土砂龙|角龙|黑角龙|眩鸟|浮空龙|水妖鸟|麒麟|溟波龙|大痹贼龙|骨锤龙|硫斩龙|雾瘴尸套龙|黑轰龙|岩贼龙|熔岩龙|爆锤龙|碎龙|红莲爆鳞龙|痹毒龙|冰牙龙|霜翼风漂龙|狱狼龙
for name in uni:
  print(name, uni.get(name))
  if len(uni.get(name)) == 1:
    un.append(name)
print(un)
