import re, requests, json, sys, time
from bs4 import BeautifulSoup
sqls = []
wps = []

wpType = 254
icon = 2471
nameArr = []
with open(r'D:\pro\script\python\weapon\3_weapon\sql\254.json', 'r', encoding='utf-8') as inf:
  for il in inf.readlines():
    jd = json.loads(il)
    [name, url, attack, affinity, defense, slots, whets] = jd
    if '铠罗' in name and ('水' in name or '冰' in name or '雷' in name or '火' in name or '援' in name):
      print('name', name)
      if not defense:
        defense = 0
      slotStr = ','.join(slots)
      slotStr = slotStr.replace('66', '1').replace('67', '2').replace('68', '3').replace('72', '4')
      arr = []
      # for rows in whets:
      #   brr = []
      #   for wh in rows:
      #     # aw = wh[0]+':'+str(wh[1])
      #     brr.append(str(wh[1]))
      #   arr.append(','.join(brr))
      # whet = '|'.join(arr)
      whet = whets
      if not name in nameArr:
        nameArr.append(name)
        sq = "insert into t_weapon values (null,'{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},{},'{}','{}',{},{},{})".format(name,'','','',12,attack,40,affinity,'water:(450)','',slotStr,'desc',whet,'','',wpType,'',1,1,'','',1, 0, icon)
        wps.append(sq)
      else:
        print('key', name, url)
  with open(r'D:\pro\note1\wp\254_wp.sql', 'w', encoding='utf-8') as out:
    for line in wps:
      out.write(line+';\n')
