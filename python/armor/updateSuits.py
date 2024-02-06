import re
with open(r'D:\git_me\script\python\armor\data\up_armor.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\armor\data\t_armor.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      [id, name, suits ] = ss.split('\t')
      print(name, suits)
      suits = '|'.join(list(map(lambda x: x.split(':')[0].replace(';',':'), suits.split('|'))))
      sl = "update t_armor set suits = '{}' where id = {};".format(suits, id)
      out.write(sl + '\n')