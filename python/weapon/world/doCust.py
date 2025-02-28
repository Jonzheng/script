
with open(r'D:\git_pro\note\mhw\3_weapon\sql\cust\254_cust.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\254.sql', 'r', encoding='utf-8') as inf:
      for aa in inf.readlines():
        if 't_wp_custom' in aa:
          out.write(aa)

