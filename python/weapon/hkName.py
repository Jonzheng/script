import json
sqls = []
mp = {}

dd = {
  '屍':'尸',
  '龍':'龙',
  '飛':'飞',
  '風':'凤',
  '雙':'双',
  '鎚':'锤',
  '槍':'枪',
  '長':'长',
  '榕':'熔',
  '軍':'军',
  '極':'极',
  '淵':'渊',
  '藪':'薮',
  '惡':'恶',
  '靈':'灵',
  '燈':'灯',
  '業':'业',
  '慾':'欲',
  '剛':'刚',
  '滅':'灭',
  '盡':'尽',
  '髮':'发',
  '獅':'狮',
  '堅':'坚',
  '殲':'歼',
  '騎':'骑',
  '輪':'轮',
  '寶':'宝',
  '紋':'纹',
  '體':'体',
  '術':'术',
  '氣':'气',
  '達':'达',
  '強':'强',
  '彈':'弹',
  '擊':'击',
  '護':'护',
  '迴':'回',
  '戰':'战',
  '結':'结',
  '砲':'炮',
  '鎧':'铠',
  '羅':'罗',
  '轉':'转',
  '銀':'银',
  '劍':'剑',
  '痺':'痹',
  '賊':'贼',
  'a':'阿尔法',
  'b':'贝塔',
  'α':'阿尔法',
  'β':'贝塔',
  'γ':'伽马'
  }
with open(r'D:\pro\script\python\weapon\data\t_wp_name_hk.txt', 'r', encoding='utf-8') as inf:
  for ol in inf.readlines():
    ol = ol.strip()
    if ol:
      [name, hk] = ol.split('\t')
      hk = hk.replace('凶豺', '贼')
      hk = hk.replace('凶顎', '痹贼')
      hk = hk.replace('花朵之刀', '鲜花之刃')
      hk = hk.replace('魔物', '怪物')
      hk = hk.replace('皇后盔', '皇后冠')
      hk = hk.replace('大牙', '巨齿')
      hk = hk.replace('火焰彎刀', '火炎弯刀')
      hk = hk.replace('火焰銳劍', '火炎锐剑')
      hk = hk.replace('泥岩龍密叢', '泥岩龙密丛')
      hk = hk.replace('泥岩龍', '泥鱼龙')
      hk = hk.replace('單手劍', '片手剑')
      hk = hk.replace('花朵小刀', '鲜花匕首')
      hk = hk.replace('小刀', '匕首')
      hk = hk.replace('水流匕首', '水流小刀')
      hk = hk.replace('閃耀匕首', '閃耀小刀')
      hk = hk.replace('冰結匕首', '冰結小刀')
      hk = hk.replace('皇后匕首', '皇后短剑')
      hk = hk.replace('蒼星的太刀', '苍星太刀')
      hk = hk.replace('鉻鋼切刀', '铬钢切刀1')
      hk = hk.replace('铬钢切刀1Ⅱ', '铬钢切刀2')
      hk = hk.replace('狩魔獵人', '猎魔人')
      hk = hk.replace('收割者', '死神')
      hk = hk.replace('鬼鐵', '鬼铁1')
      hk = hk.replace('鬼铁1Ⅱ', '鬼铁2')
      hk = hk.replace('鬼铁1Ⅲ', '鬼铁3')
      hk = hk.replace('大鬼铁1Ⅰ', '大鬼铁1')
      hk = hk.replace('大鬼铁1Ⅱ', '大鬼铁2')
      hk = hk.replace('爆鎚粉碎者', '爆锤破坏者')
      hk = hk.replace('土砂龍粉碎者', '土砂龙破坏者')
      hk = hk.replace('硬梆梆的針山', '钢针锤')
      hk = hk.replace('悲哀的重槍', '悲哀重枪')
      hk = hk.replace('愚欲的銃槍', '愚欲铳枪')
      hk = hk.replace('凶靈之柱', '亡灵之柱')
      hk = hk.replace('亡靈之柱', '凶灵之柱')
      hk = hk.replace('泥岩戰斧', '泥岩斧')
      hk = hk.replace('爆鎚戰斧', '爆锤斧')
      hk = hk.replace('命運劍斧', '塔纳托斯剑斧')
      hk = hk.replace('壞滅一束【裂】', '坏灭一束【裂】')
      hk = hk.replace('壞滅一束', '坏灭之一束')
      hk = hk.replace('深沉泥岩', '深沉泥鱼')
      hk = hk.replace('暴虐的盾斧', '暴虐盾斧')
      hk = hk.replace('皇后武器', '皇后武装')
      hk = hk.replace('惡【VICE】', '恶【罪恶】')
      hk = hk.replace('暴徒的凶弓', '暴徒凶弓')
      hk = hk.replace('充能斧', '盾斧')
      hk = hk.replace('滅盡龍輕弩', '灭尽龙轻弩炮')
      hk = hk.replace('吸血鎖鎌', '暗红锁镰')
      hk = hk.replace('輕弩槍', '轻弩炮')
      hk = hk.replace('浮空龍迅擊弩', '浮空龙迅击弩1')
      hk = hk.replace('浮空龙迅击弩1Ⅱ', '浮空龙迅击弩2')
      hk = hk.replace('泥鱼龙輕弩', '泥鱼龙子弹弩')
      hk = hk.replace('隱密輕弩', '隐密子弹弩')
      hk = hk.replace('熔岩輕弩', '熔岩子弹弩')
      hk = hk.replace('巨型十字槍', '巨型十字弩炮')
      hk = hk.replace('瘋狂的悲嘆', '疯狂悲叹')
      hk = hk.replace('麒麟筒', '幻兽筒')
      hk = hk.replace('幻兽筒【三界三禍】', '麒麟筒【三界三禍】')
      hk = hk.replace('暴食的重弩', '暴食重弩')
      hk = hk.replace('水流風笛', '水流风笛1')
      hk = hk.replace('水流风笛1Ⅱ', '水流风笛2')
      hk = hk.replace('水流风笛1Ⅲ', '水流风笛3')
      hk = hk.replace('帝王金', '皇金')
      nr = name
      hr = hk
      for n in name:
        if n in hk:
          nr = nr.replace(n, '')
      for n in hk:
        if n in name:
          hr = hr.replace(n, '')
      if len(nr) == len(hr):
        i = 0
        for k in hr:
          if not mp.get(k):
            mp[k] = nr[i]
            print(k, nr[i])
          i += 1
      else:
        print('-' * 11)
        print(name, hk)
        print('-' * 11)
for d in dd:
  if not mp.get(d):
    mp[d] = dd.get(d)
with open(r'D:\pro\script\python\weapon\data\_hk.txt', 'w', encoding='utf-8') as out:
  json.dump(mp, out, ensure_ascii=False,)