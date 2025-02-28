import re
with open(r'D:\git_pro\note\mhw\3_weapon\sql\craft\t_weaponss.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\craft\t_weapon.sql', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      if 'INSERT INTO' in ss:
        ol = re.sub(r'VALUES \(\d+, ', "VALUES (null, ", ss)
        out.write(ol)
