import json

mp = {}
with open(r'D:\git_me\script\python\quest\data\0questData.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip()
    [name, pre] = line.split('\t')
    mp[name] = pre
with open(r'D:\git_me\script\python\quest\data\0unlockDataHR.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip()
    [name, pre] = line.split('\t')
    mp[name] = pre
mon = {}
with open(r'D:\git_me\script\python\monster\data\t_monster.txt', 'r', encoding='utf-8') as inf:
  for line in inf.readlines():
    line = line.strip()
    [name, nameEn] = line.split('\t')
    mon[nameEn] = name

type = '斗技大会'
with open(r'D:\git_me\script\python\quest\data\Arena.txt', 'r', encoding='utf-8') as inf:
  with open(r'D:\git_me\script\python\quest\sql\Arena.sql', 'w', encoding='utf-8') as out:
    for line in inf.readlines():
      line = line.strip().strip(';')
      if line:
        dd = json.loads(line)
        [rank, icon, questName, minRank, zenny, timeLimit, skill, stage, client, target, failCondit, monEn, rewards, name_en, name_jp] = dd
        pre = mp.get(questName, '')
        ms = monEn.split('|')
        mrr = []
        for mn in ms:
          mz = mon.get(mn, '')
          if mz:
            mrr.append(mz)
        monEn = '|'.join(mrr)
        sql = "insert into t_quest values (null, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}')".format(rank, icon, type, questName, minRank, client, stage, monEn, rewards, failCondit, target, timeLimit, zenny, pre, name_en, name_jp)
        out.write(sql+';\n')