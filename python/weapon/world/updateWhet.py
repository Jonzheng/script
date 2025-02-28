import re
from functools import reduce
# ss = 'danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:10,dark:50|danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:60,dark:0'

# s1 = 'danger:60,warning:50,yellow:80,success:60,dark:150|danger:60,warning:50,yellow:80,success:110,dark:100'
# res = re.findall('purple:\d+', s1)
sqls = []
with open(r'D:\my_dev\script\python\weapon\t_wp.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, eld, slot, whet] = ol.split('\t')
      eld = eld.replace('龙封力[', '').replace(']', '')
      slot = slot.replace('67', '1').replace('68', '2').replace('69', '3').replace('73', '4').replace('66', '1').replace('72', '4')
      arr = []
      brr = []
      q1 = re.findall('danger:\d+', whet)
      q2 = re.findall('warning:\d+', whet)
      q3 = re.findall('yellow:\d+', whet)
      q4 = re.findall('success:\d+', whet)
      q5 = re.findall('blue:\d+', whet)
      q6 = re.findall('white:\d+', whet)
      q7 = re.findall('white:\d+', whet)
      q8 = re.findall('dark:\d+', whet)
      for k in ['danger:\d+', 'warning:\d+', 'yellow:\d+','success:\d+','blue:\d+','white:\d+', 'purple:\d+']:
        qrr = re.findall(k, whet)
        if len(qrr) == 2:
          [qq, ww] = qrr
          arr.append(qq.split(':')[1])
          brr.append(ww.split(':')[1])
        elif len(q1) == 1:
          arr.append(qq.split(':')[1])
          brr.append('0')
        else:
          arr.append('0')
          brr.append('0')
      sum1 = reduce(lambda x, y: int(x)+int(y), arr)
      sum2 = reduce(lambda x, y: int(x)+int(y), brr)
      if sum1 != 0 and sum2 != 0:
        whet = ','.join(arr)+'|'+','.join(brr)
        # print(id, eld, slot, ':', sum1, sum2)
        sql = "update t_weapon set seal = '{}', slot = '{}', whet = '{}' where id = {};\n".format(eld, slot, whet, id)
        sqls.append(sql)

with open(r'D:\my_dev\script\python\weapon\t_up_whet.sql', 'w', encoding='utf-8') as out:
  for ol in sqls:
    out.write(ol)