names = []
def getName(line):
  s1 = line.split("null,'")
  s2 = s1[1].split("'")
  return s2[0]
with open(r'D:\git_pro\note\mhw\3_weapon\sql\lsw_wp.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\lsw.sql', 'r', encoding='utf-8') as inf:
    with open(r'D:\git_pro\note\mhw\3_weapon\sql\lsw2.sql', 'r', encoding='utf-8') as inf2:
      for aa in inf.readlines():
        if 't_weapon' in aa:
          name = getName(aa)
          if not name in names:
            names.append(name)
            out.write(aa)
      for aa in inf2.readlines():
        if 't_weapon' in aa:
          name = getName(aa)
          if not name in names:
            names.append(name)
            out.write(aa)
print(names)
