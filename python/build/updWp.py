wm = {}
with open(r'D:\pro\script\python\build\data\wid_name.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, name] = ol.split('\t')
      wm[id] = name

mp = {}
with open(r'D:\pro\script\python\build\data\upd_build_wp.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\build\data\t_bd_gear.txt', 'r', encoding='utf-8') as inf:
    for ol in inf.readlines():
      ol = ol.strip()
      if ol:
        [id, type, gear] = ol.split('\t')
        wid = gear.split(',')[0]
        k = type +'|'+ wid
        wp = wm.get(wid, '')
        sql = "update t_build set wp = '{}' where id = {};\n".format(wp, id)
        # out.write(sql)
        if mp.get(k):
          mp[k] += 1
        else:
          mp[k] = 1
arr = []
for k in mp:
  if mp[k] > 0:
    [type, wid] = k.split('|')
    c = mp[k]
    arr.append({ 'type': type, 'wid': wid, 'c': c })
brr = [it for it in arr if it['type'] == '253']
crr = sorted(brr, key=lambda x: x['c'], reverse=True)
ids = []
for it in crr:
  ids.append(wm[it['wid']])
print(ids[:10])
