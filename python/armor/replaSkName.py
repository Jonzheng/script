with open(r'D:\git_me\script\python\armor\data\t_armor1.sql', 'w', encoding='utf-8') as out:
  with open(r'D:\git_me\script\python\armor\data\t_armor.sql', 'r', encoding='utf-8') as inf:
    for name in inf.readlines():
      name = name.replace('すりんがーそうてんすうあっぷ', '投射器装填数提升').replace('きんじしのどき', '金狮子的怒气')
      name = name.replace('どうりょくげん', '蓄电池').replace('さばいばー', '生还者')
      name = name.replace('まんぷくのしゅくふく', '万福的祝福').replace('せきりゅうのふういん', '冥赤龙的封印')
      name = name.replace('だいかんしゃのしゅくふく', '大感谢的祝福').replace('まんかいのしゅくふく', '盛放之祝福')
      name = name.replace('じょうねつのしゅくふく', '热情的祝福').replace('ほらーないとのしゅくふく', '惊魂夜的祝福')
      name = name.replace('きんじしのとうし', '金狮子的斗志').replace('さいりゅうのとうし', '碎龙之斗志')
      name = name.replace('らんきりゅうのしんずい', '绚辉龙的真髓').replace('ひょうがりゅうのぜつぎ', '冰牙龙的绝技')
      name = name.replace('こうこくりゅう的しんぴ', '煌黑龙的神秘')
      name = name.replace('にゅーわーるど', '新世界')
      out.write(name)