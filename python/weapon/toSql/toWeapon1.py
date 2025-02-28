
with open(r'D:\pro\script\python\weapon\sql\r_wp2423.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\pro\script\python\weapon\data2\base2423.txt', 'r', encoding='utf-8') as inf:
    for ss in inf.readlines():
      ss = ss.strip('\n')
      [name, hk, en, jp, rare, att, dff, aff, ele, whet, tree, slot, d_slot, d_sk,desc, to] = ss.split('\t')
      ele = ele.replace('无', '').replace('水', ' water:').replace('雷', ' thunder:').replace('冰', ' ice:').replace('火', ' fire:').replace('睡眠', ' sleep:').replace('毒', ' poison:').replace('龙', ' dragon:')
      ele = ele.strip()
      en = en.replace('\'', '.')
      sql = "insert into r_weapon (name, hk, en, jp, rarity, attack, defense, affinity, element, whet, tree, slot, d_slot, d_skill,`desc`, `to`) values ('{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, hk, en, jp, rare, att, dff, aff, ele, whet, tree, slot, d_slot, d_sk,desc, to)
      out.write(sql + ';\n')

'''
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NULL DEFAULT NULL,
  `tree` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '衍生类型',
  `pre` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '父武器',
  `to` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '子武器',
  `rarity` tinyint(1) NULL DEFAULT 1 COMMENT '稀有度',
  `attack` int NULL DEFAULT 1 COMMENT '攻击力',
  `defense` tinyint(1) NULL DEFAULT 0 COMMENT '防御力',
  `affinity` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '会心率',
  `element` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '属性',
  `slot` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '镶嵌槽',
  `d_slot` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '百龙槽',
  `d_skill` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '百龙技能',
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '武器描述',
  `whet` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '斩味或弹药',
  `unlock` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '解锁条件',
  `skill` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '技能名称',
  `type` int NULL DEFAULT NULL COMMENT '武器类型',
  `music` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '笛子演奏效果或者弩偏移',
  `gun_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '炮击类型或特殊弹药',
  `gun_lv` tinyint(1) NULL DEFAULT 1 COMMENT '炮击等级',
  `create` tinyint(1) NULL DEFAULT 0 COMMENT '是否直接生产',
  `icon` int NULL DEFAULT NULL COMMENT '预览图',
  `hk` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '繁体名称',
  `en` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '英文名称',
  `jp` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '日文名称',

'''