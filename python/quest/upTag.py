
with open(r'D:\git_me\script\python\quest\data\t_quest0.txt', 'r', encoding='utf-8') as inf:
  with open(r'D:\git_me\script\python\quest\sql\up_tag.sql', 'w', encoding='utf-8') as out:
    for line in inf.readlines():
      line = line.strip()
      [id, rank, name, rwd] = line.split('\t')
      tag = rwd.split(':')[0]
      sql = "update t_quest set tag = '{}' where id = {};#{}".format(tag, id, name)
      out.write(sql+'\n')
