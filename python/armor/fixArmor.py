
import json
# ["225", "170-188|208", "2", "2", "0", "0", "3", "4", "体术:2|集中:1", "精英·苍世武士【羽织】阿尔法", "银火龙的真髓:2:投射器装填·极意|银火龙的真髓:4:真·会心击【属性】", "苍世的大宝玉:1|银白霜雪之毛皮:2|白银之冰刃牙:1|冰晶的厚龙鳞:3"];

rarity = 12
with open(r'D:\git_me\script\python\armor\dress\fix_armor.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\armor\data\armorfix.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      ss = ss.strip().strip(';')
      arr = json.loads(ss)
      [icon, defence, fire, water, thunder, ice, dragon, slots, skill, name, suits, craft] = arr
      sql = "insert into t_armor values (null, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', {}, {}, {}, {}, {});\n".format(name, slots, skill, suits, rarity,icon, craft, defence, fire, water, thunder, ice, dragon )
      out.write(sql)

