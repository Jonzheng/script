with open(r'D:\pro\script\python\weapon\data2\cft2421.txt', 'r', encoding='utf-8') as inf1:
  with open(r'D:\pro\script\python\weapon\data2\cft2422.txt', 'r', encoding='utf-8') as inf2:
    with open(r'D:\pro\script\python\weapon\data2\cft2423.txt', 'r', encoding='utf-8') as inf3:
      with open(r'D:\pro\script\python\weapon\sql\r_wp_craft1.sql', 'w', encoding='utf-8') as out:
        lrr = inf1.readlines() + inf2.readlines() + inf3.readlines()
        for ss in lrr:
          ss = ss.strip()
          srr = ss.split('\t')
          [name, items, unlock, zenny, buy, create] = srr
          if not buy:
            buy = 0
          if not zenny:
            zenny = 0
          sql = "insert into r_wp_craft (name, items, `unlock`, zenny, buy, `create`) values ('{}', '{}', '{}', {}, {}, {});\n".format(name, items, unlock, zenny, buy, create)
          out.write(sql)