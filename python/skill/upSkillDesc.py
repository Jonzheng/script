
with open(r'D:\git_me\script\python\skill\data\up_sk_desc.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\skill\data\skill-des.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      [id, name, desc ] = ss.strip().split('\t')
      sl = "update t_armor set `desc` = '{}' where id = {};".format(desc, id)
      out.write(sl + '\n')