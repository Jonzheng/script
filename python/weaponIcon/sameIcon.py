import photohash, os, re

path=r'D:\my_dev\script\python\weaponIcon\out\254'
path2=r'D:\my_dev\script\python\weaponIcon\out\254i'

files = os.listdir(path)
sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(path, x)))

hp = {}
sqls = []
for fn in sorted_files:
  hashCode = photohash.average_hash(os.path.join(path, fn))
  # newName = fn.replace("242-","")
  [id] = re.findall("\d+",fn)
  # os.rename(os.path.join(path,fn), os.path.join(path,newName))
  if not hp.get(hashCode):
    hp[hashCode] = id
    print('origin:', fn)
    ss = "update t_weapon set icon = {} where id = {}".format(id, id)
    print('1', ss)
    sqls.append(ss)
    os.rename(os.path.join(path,fn), os.path.join(path2,fn))
  else:
    print('same', fn, hp[hashCode])
    ss = "update t_weapon set icon = {} where id = {}".format(hp[hashCode], id)
    print('2', ss)
    sqls.append(ss)

# for file in os.listdir(path):
#   hashCode = photohash.average_hash(os.path.join(path, file))
#   print(hashCode, file)

with open(r'D:\my_dev\script\python\weaponIcon\out\t_icon_254.sql', 'w', encoding='utf-8') as out:
  for line in sqls:
    out.write(line+';\n')