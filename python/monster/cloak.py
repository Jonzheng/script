with open(r'D:\git_pro\note\mhw\0_monsters\cloak.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\0_monsters\cloak.txt', 'r', encoding='utf-8') as inf:
      for line in inf.readlines():
          [name, desc, condit, type, cd] = line.split('\t')
          sql2 = "insert into t_cloak (slot, name, `desc`, condit, cd, `type`) values('{}','{}','{}','{}','{}','{}');\n".format('', name, desc, condit, cd.strip(), type)
          out.write(sql2)