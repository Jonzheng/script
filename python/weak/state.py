mp = {}
with open(r'D:\git_pro\note\mhw\0_monsters\monid.txt', 'r', encoding='utf-8') as inf:
    for le in inf.readlines():
        [id, name, en] = le.strip().split(';')
        mp[en.lower()] = name

# with open(r'D:\git_pro\note\mhw\2weak\t_weakness.sql', 'w', encoding='utf-8') as out:
cc = 0
brr = []
drr = []
with open(r'D:\git_pro\note\mhw\2weak\weak2.tsv', 'r', encoding='utf-8') as inf:
    for lne in inf.readlines():
        arr = lne.split('\t')
        # print(len(arr), arr)
        [idx, name, q, cate, w, poison, sleep, paralysis, blast, stun, a,s,d,f,g,h,j,z,x,c] = arr[:20]
        name = mp.get(name.lower())
        # print(name, cate, poison, sleep, paralysis, blast, stun)
        if "|" in q:
            cc +=1
            # print(name, poison, sleep, paralysis, blast, stun)
            brr = [[name, poison], [name, sleep], [name, paralysis], [name, blast], [name, stun]]
        elif 'Duration' == cate:
            cc += 1
            idx = 5
            for it in brr:
              it.append(arr[idx])
              idx += 1
        elif 'Initial Tolerance' == cate:
            cc += 1
            idx = 5
            for it in brr:
              it.append(arr[idx])
              idx += 1
        elif 'Tolerance Increase' == cate:
            idx = 5
            for it in brr:
              it.append(arr[idx])
              idx += 1
        elif 'Max Tolerance' == cate:
            cc += 1
            idx = 5
            for it in brr:
              it.append(arr[idx])
              idx += 1
        elif 'Damage' == cate:
            cc += 1
            idx = 5
            for it in brr:
              it.append(arr[idx])
              idx += 1
            drr.append(brr)

print('--end', cc)

dp = {1:'poison', 2:'sleep', 3:'paralysis', 4:'blast', 5:'stun'}
with open(r'D:\git_pro\note\mhw\2weak\t_state.sql', 'w', encoding='utf-8') as out:

  for brr in drr:
    i = 0
    for ld in brr:
      i += 1
      [q,w,e,r,t,y,u] = ld
      build = '–'
      if not '✖' == w:
        build = "{}+{}→{}".format(r,t,y)
      print(q, dp.get(i), w, e, build, u) # ✖ – –+–→– – ✖ – - –
      sql = "insert into t_state (monster_name, `state`, `weak`, dura, build, damage) values('{}','{}','{}','{}','{}','{}');\n".format(q, dp.get(i), w, e, build, u)
      out.write(sql)