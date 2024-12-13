
wbm = {}
with open(r'D:\pro\script\python\build\data\t_id_skied.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [id, skied] = ol.split('\t')
      if '冰呪龙的神秘' in skied:
        wbm[id] = 1
print(wbm)
with open(r'D:\pro\script\python\build\data\upd_build_suit.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\build\data\t_bd_gear.txt', 'r', encoding='utf-8') as inf:
    for ol in inf.readlines():
      ol = ol.strip()
      if ol:
        [id, type, gear] = ol.split('\t')
        suit = []
        grr = gear.split(',')[1:6]
        # print('---', id,wbm.get(id), gear, grr)
        mn = 0
        for aid in range(192, 202):
          if str(aid) in grr:
            mn += 1
        if mn > 3:
          suit.append('黑龙4件套')
        elif mn > 1:
          suit.append('黑龙2件套')
        wbn = 0
        for aid in range(187, 192):
          if str(aid) in grr:
            wbn += 1
        for aid in range(1, 11):
          if str(aid) in grr:
            wbn += 1
        if wbm.get(id):
          wbn += 1
        if wbn > 3:
          suit.append('冰咒龙4件套')
        elif wbn > 1:
          suit.append('冰咒龙2件套')
        mcn = 0
        for aid in range(141, 151):
          if str(aid) in grr:
            mcn += 1
        if mcn > 4:
          suit.append('冥赤龙5件套')
        elif mcn > 2:
          suit.append('冥赤龙3件套')
        mcn = 0
        for aid in range(151, 161):
          if str(aid) in grr:
            mcn += 1
        if mcn > 2:
          suit.append('煌黑龙3件套')
        elif mcn > 1:
          suit.append('煌黑龙2件套')
        ywn = 0
        for aid in range(21, 31):
          if str(aid) in grr:
            ywn += 1
        if ywn > 2:
          suit.append('炎王龙3件套')
        yn = 0
        for aid in range(176, 186):
          if str(aid) in grr:
            yn += 1
        if yn > 2:
          suit.append('轰龙3件套')
        hlc = 0
        for aid in range(386, 396):
          if str(aid) in grr:
            hlc += 1
        if hlc > 2:
          suit.append('冰牙龙3件套')
        elif hlc > 0:
          suit.append('冰牙龙1件套')
        if len(suit) > 0:
          # print(id, '+'.join(suit))
          sql = "update t_build set suit = '{}' where id = {};\n".format('+'.join(suit), id)
          out.write(sql)