import re
from functools import reduce
# ss = 'danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:10,dark:50|danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:60,dark:0'

# s1 = 'danger:60,warning:50,yellow:80,success:60,dark:150|danger:60,warning:50,yellow:80,success:110,dark:100'
# s1 = 'danger:140,warning:30,yellow:30,success:60,blue:50,white:40,dark:50|danger:140,warning:30,yellow:30,success:60,blue:50,white:40,purple:50,dark:0'
# res = re.findall('white:\d+', s1)
# print(res)
mp = {}
with open(r'D:\git_me\script\python\weapon\data\t_weapon.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    [id, whet] = ol.strip().split('\t')
    mp[id] = whet

sqls = []
ddd = []
with open(r'D:\git_me\script\python\weapon\t_wp.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, eld, slot, whet] = ol.split('\t')
      q1 = re.findall(r'danger:\d+', whet)
      q2 = re.findall(r'warning:\d+', whet)
      q3 = re.findall(r'yellow:\d+', whet)
      q4 = re.findall(r'success:\d+', whet)
      q5 = re.findall(r'blue:\d+', whet)
      q6 = re.findall(r'white:\d+', whet)
      q7 = re.findall(r'purple:\d+', whet)
      q8 = re.findall(r'dark:\d+', whet)
      # print(q1, q2, q3, q4, q5, q6, q7, q8)
      arr = []
      brr = []
      for qrr in [q1, q2, q3, q4, q5, q6, q7, q8]:
        if len(qrr) == 2:
          [qq, ww] = qrr
          arr.append(qq.split(':')[1])
          brr.append(ww.split(':')[1])
        elif len(qrr) == 1:
          [qq] = qrr
          if qq in whet.split('|')[0]:
            arr.append(qq.split(':')[1])
            brr.append('0')
          else:
            brr.append(qq.split(':')[1])
            arr.append('0')
        else:
          arr.append('0')
          brr.append('0')
      sum1 = reduce(lambda x, y: int(x)+int(y), arr)
      sum2 = reduce(lambda x, y: int(x)+int(y), brr)
      if sum1 != 0 and sum2 != 0:
        whet = ','.join(arr)+'|'+','.join(brr)
        print(id, whet, '===', mp.get(id))
        if mp.get(id) and mp.get(id) != whet:
          sql = "update t_weapon set whet = '{}' where id = {};\n".format(whet, id)
          sqls.append(sql)
        else:
          sql = "update t_weapon set whet = '{}' where id = {};\n".format(whet, id)
          ddd.append(sql)


with open(r'D:\git_me\script\python\weapon\sql\update_whet.sql', 'w', encoding='utf-8') as out:
  for ol in sqls:
    out.write(ol)
    
with open(r'D:\git_me\script\python\weapon\sql\update_whet333.sql', 'w', encoding='utf-8') as out:
  for ol in ddd:
    out.write(ol)