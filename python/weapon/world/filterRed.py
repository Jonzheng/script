import re
with open(r'python/weapon/data/t_weapon_red.sql', 'w', encoding='utf-8') as out:
  with open(r'python/weapon/data/t_weapon_notree.sql', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      if '赤龙' in ss:
        pattern = re.compile('(?<=VALUES \().*?(,)')
        ret = pattern.sub('null,', ss)
        out.write(ret)
