arr = []

with open(r'D:\git_pro\note\mhw\3_weapon\sql\arr\253.js', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      arr.append("'{}'".format(ol))
def getName(line):
  s1 = line.split("null,'")
  s2 = s1[1].split("'")
  return s2[0]

nrr = []
brr = []
with open(r'D:\git_pro\note\mhw\3_weapon\sql\253_wp.sql', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    if ol:
      brr.append(ol)

crr = []
frr = []
for tree in arr:
  for ol in brr:
    name = getName(ol)
    if tree in ol and not name in frr:
      frr.append(name)
      crr.append(ol)

drr = ['\n','\n']

for ol in brr:
  if not ol in crr:
    name = getName(ol)
    if name not in nrr:
      nrr.append(name)
      drr.append(ol)

print(nrr)

with open(r'D:\git_pro\note\mhw\3_weapon\sql\wp\253.sql', 'w', encoding='utf-8') as out:
  for ol in crr:
    out.write(ol)
  for ol in drr:
    out.write(ol)