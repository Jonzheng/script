
names = []
print('len', len(names))
s1 = []
s2 = []
s3 = []
with open(r'D:\pro\script\python\item\data\r_craft1.txt', 'r', encoding='utf-8') as inf1:
  with open(r'D:\pro\script\python\item\data\r_craft2.txt', 'r', encoding='utf-8') as inf2:
      with open(r'D:\pro\script\python\item\data\r_craft4.txt', 'r', encoding='utf-8') as inf4:
        with open(r'D:\pro\script\python\item\data\r_craft6.txt', 'r', encoding='utf-8') as inf6:
            with open(r'D:\pro\script\python\item\data\r_craft7.txt', 'r', encoding='utf-8') as inf7:
              with open(r'D:\pro\script\python\item\sql\r_craft1.sql', 'w', encoding='utf-8') as out:
                lrr = inf7.readlines() + inf1.readlines() + inf2.readlines() + inf4.readlines() + inf6.readlines()
                for ss in lrr:
                  ss = ss.strip()
                  srr = ss.split('\t')
                  kk = ','.join(srr)
                  if kk not in names:
                    names.append(kk)
                    if len(srr) == 4:
                      [kv1, kv2, name, quantity] = srr
                      sql = "insert into r_craft (name, kv1, kv2, quantity) values ('{}', '{}', '{}', {})".format(name, kv1, kv2, quantity)
                      out.write(sql + ';\n')
                  else:
                    print('k', kk)