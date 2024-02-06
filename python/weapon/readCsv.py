nameMp = {}
with open(r'D:\git_me\script\python\weapon\data\weapon_b_translations.csv', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    arr = ss.strip().split('\t')
    [en, zh] = arr
    nameMp[en] = zh
wpMp = {}
with open(r'D:\git_me\script\python\weapon\data\weapon_base.csv', 'r', encoding='utf-8') as inf:
  for ss in inf.readlines():
    arr = ss.strip().split(',')
    [id,name_en,weapon_type,previous_en,category,rarity,attack,affinity,defense,element_hidden,element1,element1_attack,element2,element2_attack,elderseal,slot_1,slot_2,slot_3,kinsect_bonus,phial,phial_power,shelling,shelling_level,notes,ammo_config,skill] = arr
    if "Kjárr" in name_en and '12' == rarity:
      print(name_en, '|', rarity)
      # sq = "insert into t_weapon values (null,'{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}',{})".format(name,tree_en,pre,to,rarity,attack,defense,affinity,element,elderseal,slotStr,desc,whet,unlock,skill,wpType,name_hk,cust,music,gunType,gunLv)
      if nameMp.get(name_en):
        wpMp[nameMp.get(name_en)] = [attack,affinity,defense,element1,element1_attack,element2,element2_attack,elderseal]

with open(r'D:\git_me\script\python\weapon\data\t_weapon_gold.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\weapon\data\t_weapon_notree.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      arr = ss.strip().split('\t')
      [id,name,tree_en,pre,to,rarity,attack,defense,affinity,element,elderseal,slotStr,desc,whet,unlock,skill,wpType,name_hk,cust,music,gunType,gunLv,create,icon] = arr
      if '皇金' in name:
        brr = wpMp.get(name_hk)
        print(name, attack,affinity,defense,element,elderseal, 'vs', brr)
        attack = brr[0]
        affinity = brr[1]
        defense = brr[2]
        if brr[3]:
          element = brr[3].lower() + ':' + brr[4]
        if whet:
          ww1 = whet.split('|')[1]
          whet = ww1 + '|' + ww1
        rarity = 12
        sq = "insert into t_weapon values (null,'{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}',{},{},{})".format(name,tree_en,pre,to,rarity,attack,defense,affinity,element,elderseal,slotStr,desc,whet,unlock,skill,wpType,name_hk,cust,music,gunType,gunLv,create,icon)
        out.write(sq+'\n;')
