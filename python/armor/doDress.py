
brr = []
import json
rarity = 1
with open(r'D:\git_me\script\python\armor\dress\dress1.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\armor\data\t_bak1.js', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      ss = ss.strip().strip(';')
      arr = json.loads(ss)
      name = arr[-3]
      craft = arr[-1]
      # print(name, craft)
      if '黎明武士' not in name:
        name = name.split('】')[0].strip('【')
      key = name + craft
      if key not in brr and craft:
        brr.append(key)
        print(name, craft)
        sql = "insert into t_dress values (null, {}, 231, '{}', '{}');\n".format(rarity, name, craft)
        out.write(sql)