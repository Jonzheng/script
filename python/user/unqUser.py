
ops = []
ids = []
with open(r'D:\git_me\script\python\user\t_user.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines()[39999:40002]:
    line = line.strip()
    [id, opid] = line.split('\t')
    if opid not in ops:
      ops.append(opid)
    else:
      ids.append(int(id))


import json
with open(r'D:\git_me\script\python\user\uids.txt', 'w', encoding='utf-8') as out:
  out.write(json.dumps(ids, ensure_ascii=False))