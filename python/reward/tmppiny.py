from xpinyin import Pinyin

p = Pinyin()
result1 = p.get_pinyin('灭尽龙')

print(result1)

import os,sys

path = 'F:\怪物猎人世界怪物图标'

def rename(path):
  for dr in os.listdir(path):
    fp = os.path.join(path, dr)
    for file in os.listdir(fp):
      newName = p.get_pinyin(file.split('.')[0]) + '.png'
      print(file, newName)
      os.rename(os.path.join(fp, file), os.path.join('F:\outmhw', newName))
rename(path)
#结束

print("End")
