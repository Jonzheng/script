sqls = []
with open(r'D:\pro\script\python\charm\data\t_charm_id_sk.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, name, ski] = ol.split('\t')
      ski = ski.replace(' ', ':')
      sql = "update t_charm set skill = '{}' where id = {};\n".format(ski, id)
      sqls.append(sql)

with open(r'D:\pro\script\python\charm\data\upd_ski.sql', 'w', encoding='utf-8') as out:
  for ol in sqls:
    out.write(ol)