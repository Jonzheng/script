import re
# ss = 'danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:10,dark:50|danger:10,warning:50,yellow:50,success:50,blue:60,white:120,purple:60,dark:0'

# s1 = 'danger:60,warning:50,yellow:80,success:60,dark:150|danger:60,warning:50,yellow:80,success:110,dark:100'
# res = re.findall('purple:\d+', s1)
sqls = []
with open(r'D:\my_dev\script\python\weapon\t_wp.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, eld, slot, whet] = ol.split('\t')
      if '6' in slot or '7' in slot:
        eld = eld.replace('龙封力[', '').replace(']', '')
        slot = slot.replace('67', '1').replace('68', '2').replace('69', '3').replace('73', '4').replace('66', '1').replace('72', '4')
        sql = "update t_weapon set seal = '{}', slot = '{}' where id = {};\n".format(eld, slot, id)
        sqls.append(sql)

with open(r'D:\my_dev\script\python\weapon\t_up_slot.sql', 'w', encoding='utf-8') as out:
  for ol in sqls:
    out.write(ol)