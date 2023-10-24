from xpinyin import Pinyin
p = Pinyin()
with open(r'D:\git_pro\note\mhw\0_monsters\monicon.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\0_monsters\monid.txt', 'r', encoding='utf-8') as inf:
      for le in inf.readlines():
          [id, name, en] = le.strip().split(';')
          pn = p.get_pinyin(name) + '.png'
          print(id, name, en, pn)
          print('--')
          sql = "update t_monster set icon = '{}' where id = {};\n".format(pn,id)
          out.write(sql)