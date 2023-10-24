from zhconv import convert



with open(r'D:\git_pro\note\mhw\0_monsters\hkname.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\0_monsters\monid.txt', 'r', encoding='utf-8') as inf:
      for le in inf.readlines():
          [id, name, en] = le.strip().split(';')
          print(name, convert(name, 'zh-tw'))
          sql = "update t_monster set name_hk = '{}' where name = '{}';\n".format(convert(name, 'zh-tw'), name)
          out.write(sql)