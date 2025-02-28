import sys
tmp = {}
names = []
with open(r'python/weapon/data2/base2421.txt', 'r', encoding='utf-8') as inf:
  with open(r'python/weapon/data2/base2422.txt', 'r', encoding='utf-8') as inf2:
    with open(r'python/weapon/data2/base2423.txt', 'r', encoding='utf-8') as inf3:
      lrr = inf.readlines() + inf2.readlines() + inf3.readlines()
      for ss in lrr:
        ss = ss.strip('\n')
        [name, hk, en, jp, rare, att, dff, aff, ele, whet, tree, slot, d_slot, d_sk,desc, to] = ss.split('\t')
        names.append(name)
        if tmp.get(name):
          print(name, tmp.get(name))
        else:
          tmp[name] = to.split('|')
with open(r'D:\pro\script\python\weapon\sql\upd_wp_pre.sql', 'w', encoding='utf-8') as out:
  for name in names:
    for k in tmp:
      if name in tmp[k]:
        sql = "update r_weapon set pre = '{}' where name = '{}';\n".format(k, name)
        out.write(sql)

