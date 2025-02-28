
itNames = []
# with open(r'D:\pro\script\python\item\data\r_item1.txt', 'r', encoding='utf-8') as inf:
#   for ss in inf.readlines():
#     [name, cate, rarity, hk, en, jp, buy, sell, desc, obtain] = ss.split('\t')
#     itNames.append(name)
print('len', len(itNames))
with open(r'D:\pro\script\python\item\sql\r_item9.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\item\data\r_item9.txt', 'r', encoding='utf-8') as inf:
    tag = '搬运素材'
    for ss in inf.readlines():
      [name, cate, rarity, hk, en, jp, buy, sell, desc, obtain] = ss.split('\t')
      if name not in itNames:
        en = en.replace('\'', '.')
        buy = buy.replace('—', '0')
        sell = sell.replace('—', '0')
        sql = "insert into r_items (name, tag, cate, icon, obtain, `desc`, rarity, buy, sell, hk, en, jp) values ('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}')".format(name, tag, cate, '', obtain, desc, rarity, buy, sell, hk, en, jp)
        out.write(sql + ';\n')
      else:
        print('exist', name)
'''
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `tag` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '素材类型',
  `cate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '道具分类',
  `icon` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `obtain` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '获取途径',
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '物品说明',
  `rarity` tinyint(1) NULL DEFAULT NULL COMMENT '稀有度',
  `buy` int NULL DEFAULT NULL COMMENT '购买价格',
  `sell` int NULL DEFAULT NULL COMMENT '出售价格',
  `hk` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '繁体名称',
  `en` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '英文名称',
  `jp` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '日文名称',

UPDATE r_items
INNER JOIN t_items ON r_items.name = t_items.name
SET r_items.icon = t_items.icon;

ALTER TABLE r_items AUTO_INCREMENT = 206;

'''