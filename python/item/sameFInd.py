

uq = []
with open(r'D:\my_dev\script\python\item\sql\t_up_find.sql', 'r', encoding='utf-8') as inf:
  with open(r'D:\my_dev\script\python\item\sql\t_up_find2.sql', 'w', encoding='utf-8') as out:
    for line in inf.readlines():
      if not line in uq:
        uq.append(line)
        out.write(line)