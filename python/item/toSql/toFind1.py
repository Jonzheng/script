
names = []
print('len', len(names))
with open(r'D:\pro\script\python\item\data\r_item_find1.txt', 'r', encoding='utf-8') as inf1:
  with open(r'D:\pro\script\python\item\data\r_item_find2.txt', 'r', encoding='utf-8') as inf2:
    with open(r'D:\pro\script\python\item\data\r_item_find3.txt', 'r', encoding='utf-8') as inf3:
      with open(r'D:\pro\script\python\item\data\r_item_find4.txt', 'r', encoding='utf-8') as inf4:
        with open(r'D:\pro\script\python\item\data\r_item_find6.txt', 'r', encoding='utf-8') as inf6:
          with open(r'D:\pro\script\python\item\data\r_item_find8.txt', 'r', encoding='utf-8') as inf8:
            with open(r'D:\pro\script\python\item\data\r_item_find9.txt', 'r', encoding='utf-8') as inf9:
              with open(r'D:\pro\script\python\item\sql\r_item_find1.sql', 'w', encoding='utf-8') as out:
                lrr = inf1.readlines() + inf2.readlines() + inf3.readlines() + inf4.readlines() + inf6.readlines() + inf8.readlines() + inf9.readlines()
                for ss in lrr:
                  ss = ss.strip()
                  srr = ss.split('\t')
                  kk = ','.join(srr)
                  if kk not in names:
                    names.append(kk)
                    if len(srr) == 7:
                      [name, tag, monster_name, rank, desc, quantity, percent] = srr
                      tag = '怪物素材'
                      percent = percent.replace('%', '')
                      desc = desc.replace('・', '·')
                      quantity = quantity.replace('—', '0')
                      percent = percent.replace('—', '0')
                      sql = "insert into r_item_find (name, tag, monster_name, `rank`, `desc`, quantity, percent) values ('{}', '{}', '{}', '{}', '{}', {}, {})".format(name, tag, monster_name, rank, desc, quantity, percent)
                      out.write(sql + ';\n')
                    if len(srr) == 8:
                      [name, tag, quest_type, rank, quest_name, desc, quantity, percent] = srr
                      tag = '任务奖励'
                      percent = percent.replace('%', '')
                      desc = desc.replace('・', '·')
                      quantity = quantity.replace('—', '0')
                      percent = percent.replace('—', '0')
                      sql = "insert into r_item_find (name, tag, quest_type, `rank`, quest_name, `desc`, quantity, percent) values ('{}', '{}', '{}', '{}', '{}', '{}', {}, {})".format(name, tag, quest_type, rank, quest_name, desc, quantity, percent)
                      out.write(sql + ';\n')
'''
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `tag` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `rank` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `quantity` int NULL DEFAULT NULL COMMENT '奖励数量',
  `percent` int NULL DEFAULT NULL COMMENT '获得概率',
  `quest_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '任务类型',
  `quest_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '任务名称',
  `monster_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '怪物名称',
  `u_date` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `c_date` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `zan` int NULL DEFAULT 0,
・
·.・
·
倪泰教官的挑战书・其五
UPDATE r_items
INNER JOIN t_items ON r_items.name = t_items.name
SET r_items.icon = t_items.icon;

ALTER TABLE r_items AUTO_INCREMENT = 206;

UPDATE r_items
SET name = REPLACE(name, '・', '·')
WHERE name LIKE '%・%';

'''