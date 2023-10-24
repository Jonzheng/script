with open(r'D:\git_pro\note\mhw\0_monsters\notes.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\0_monsters\notes.txt', 'r', encoding='utf-8') as inf:
      for line in inf.readlines():
          content = line.strip()
          sql2 = "insert into t_notes (content, zan) values('{}', 0);\n".format(content)
          out.write(sql2)