import re
with open(r'D:\git_me\script\python\armor\data\up_armoricon.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\armor\data\t_armoricon.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      [id, icon ] = ss.split('\t')
      icon = int(icon) + 1
      sl = "update t_armor set icon = '{}' where id = {};".format(icon, id)
      out.write(sl + '\n')