arr1 = []
with open(r'D:\git_pro\note\mhw\item500.sql', 'r', encoding='utf-8') as inf:
   arr1 = inf.readlines()
print('len', len(arr1))
names = []
with open(r'D:\git_pro\note\mhw\t_item500.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_pro\note\mhw\t_item_find500.sql', 'w', encoding='utf-8') as out2:
    name = ''
    id = ''
    for line in arr1:
      if 't_items' in line:
        idx1 = line.index(',\'')
        sub2 = line[idx1+2:]
        name = sub2[:sub2.index('\',\'')]
        # print('name', name)
        if name not in names:
          names.append(name)
          id = line[line.index('values(')+7:idx1]
          out.write(line)
        else:
            print(name)
      else:
        ol = line.replace('item_id', 'item_name').replace('1111', "'{}'".format(name))
        out2.write(ol)