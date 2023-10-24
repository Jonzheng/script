# sql = 'insert into t_weapon_craft values '
# component = '80000 zenny|歼灭的大刚角| x 3|灭尽龙的刚爪| x 4|无穷的新生壳| x 5|古龙的大宝玉| x 1|Unlock: |歼世灭尽龙'
# cps = component.replace('| x', '').split('|')
# srr = []
# name = '皇后盔'
# for v in cps:
#   v = v.strip()
#   vs = v.split()
#   print(len(vs), vs)
#   if len(vs) != 2:
#     print('not', vs)
#     continue
#   print('in', vs)
#   if 'zenny' in v:
#     srr.append("('{}', {}, '{}')".format('金币', vs[0], name))
#   else:
#     srr.append("('{}', {}, '{}')".format(vs[0], vs[1], name))
# # sql += srr.join(',') 这是js
# sql += ','.join(srr)
# print(sql)

import re

# res = re.findall("\d+", '赋予回复能力')
# res = re.findall("\d+", '攻击力强化1|Slot: 3')
# print('s', res)
# ss = "insert into t_weapon values (null,'金色的大剑·水',6,768,20,'','water:(270)','','','用绚辉龙的金属片加工制成的大剑。具有的特性不明，无法完全激发出它的性能。','danger:190,warning:70,yellow:20,success:50,blue:20,dark:50|danger:190,warning:70,yellow:20,success:50,blue:30,white:40,dark:0','','','l_sword','','金色的大劍‧水','','',3);"
# s1 = ss.split("null,'")
# s2 = s1[1].split("'")
# print(s1)
# print(s2[0])

# h = [{'tree': '风风风', 'att': 1},{'tree': '三刀', 'att': 6},{'tree': '懂法扥', 'att': 3},{'tree': '', 'att': 2},{'tree': '掐死', 'att': 4},{'tree': '掐死', 'att': 1},{'tree': '懂法扥', 'att': 6}]
# print(sorted(h, key=lambda tup: (tup['tree'], tup['att'])))

s = "INSERT INTO `t_weapon` VALUES (1, '防卫队炎刃型大剑1', '防卫队衍生', '', '防卫队炎刃型大剑2', 1, 624, 0, '', 'blast:240', '', '', '为了防卫队制作的轻弩。集结了工房技术的精髓，得以实现前所未有的卓越性能。', 'danger:30,warning:60,yellow:20,success:90,dark:200|danger:30,warning:60,yellow:20,success:140,dark:150', '', '', 242, '防衛隊炎刃型大劍Ⅰ', 0, '', NULL, NULL, 1);"

# ret = re.sub(r'VALUES \(\d+, ', "VALUES (", s)
ret = re.sub(r'NULL', "''", s)

print(ret)