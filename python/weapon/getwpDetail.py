import re, requests, json, sys, time
from bs4 import BeautifulSoup
sqls = []
wps = []
def getItem(url, name='魂焰刚剑·灭尽'):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  wpName = name
  desc = ''
  rarity = 1
  element = ''
  tree_en = ''
  elderseal = ''
  weapon_type = ''
  name_hk = ''
  cust = 0
  unlock = ''
  skill = ''
  preWeapon = ''
  toWeapons = []
  music = []
  gunType = ''
  gunLv = 1
  shake = ''
  for cd in cards:
    head = cd.select('.card-header')
    ctext = cd.select('.card-text')
    tn = ''
    hasImg = []
    if head:
      tn = head[0].get_text().strip()
      hasImg = head[0].select('img')
    if ctext:
      desc = ctext[0].get_text().replace('\r', '').replace('\s', '').replace('\n', '').strip()
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if len(hasImg) > 0:
        for tr in trs:
          th1 = tr.select('th')[0].get_text().strip()
          td1 = tr.select('td')[0].get_text().strip()
          if th1 == 'rarity':
            rarity = td1
          elif th1 == 'tree_en':
            tree_en = td1
          elif 'element' in th1: # or 'wep_ids' in th1 双刀
            element = td1.replace('paralysis', 'paralysis:').replace('thunder', ' thunder:').replace('sleep', ' sleep:')
            element = element.replace('blast', ' blast:').replace('ice', ' ice:').replace('water', ' water:')
            element = element.replace('fire', ' fire:').replace('dragon', ' dragon:').replace('poison', ' poison:')
            if '(' in element:
              element = element.replace('(', '').replace(')', '')
              element = element.replace(':', ':(') + ')'
            element = element.strip()
          elif 'weapon_type' in th1:
            weapon_type = td1
          elif 'skill_id' in th1:
            skill = td1
          elif '龙封力' in th1:
            elderseal = td1
          elif 'wep_ids' in th1: # 铳枪
            gunType = td1.replace('减气瓶', ' 减气瓶:').replace('灭龙瓶', ' 灭龙瓶:').replace('麻痹瓶', ' 麻痹瓶:')
            # gunLv = td1.split('Lv')[1].strip()
          # elif 'music' in th1:
          #   iss = tr.select('td')[0].select('img')
          #   for im in iss:
          #     vvv = im['src'].replace('/images/music/', '').replace('.png', '')
          #     music.append(vvv)
          elif '偏移' in th1:
            shake = td1
          elif '特殊弹药' in th1:
            gunType = td1
          elif '强化部位' in th1:
            lv = td1
          elif '自定义强化' in th1:
            cust = td1
    elif 'Crafting' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        [td1, td2] = tds
        create = 0
        type = td1.get_text().strip()
        if '强化' in type:
          preWeapon = td1.select('a')[0].get_text().strip()
        elif 'Upgrade' in type:
          toWeapon = td1.select('a')[0].get_text().strip()
          toWeapons.append(toWeapon)
        elif 'Create' in type:
          create = 1
        component = td2.get_text('|').replace('\r', '').strip().replace('| x', '')
        if create == 1 or preWeapon:
          # insert into t_wp_craft values ('foo', 1),('bar', 2);
          # component 80000 zenny|歼灭的大刚角| x 3|灭尽龙的刚爪| x 4|无穷的新生壳| x 5|古龙的大宝玉| x 1|Unlock: |歼世灭尽龙
          sql = 'insert into t_wp_craft values '
          cps = component.replace('| x', '').replace('Unlock: |', 'Unlock:').split('|')
          srr = []
          for v in cps:
            v = v.strip()
            if 'Unlock' in v:
              unlock = v.replace('Unlock:', '')
            vs = v.split()
            # print(len(vs), vs)
            if len(vs) != 2:
              continue
            if 'zenny' in v:
              zn = vs[0].replace(',', '')
              srr.append("('{}', {}, '{}', {})".format('金币', zn, wpName, create))
            else:
              srr.append("('{}', {}, '{}', {})".format(vs[0], vs[1], wpName, create))
          # sql += srr.join(',') 这是js
          sql += ','.join(srr)
        if sql:
          sqls.append(sql)
        sql = ''
        # print('preWeapon', preWeapon)
        # print('component', component)
    elif '自定义强化' in tn:
      sql = 'insert into t_wp_custom values '
      srr = []
      for tr in trs:
        tds = tr.select('td')
        if not len(tds) == 2:
          continue
        [td1, td2] = tds
        sm = td1.small.extract().get_text().replace('\r', '').replace('\n', '').strip()
        augment = td1.get_text('|').replace('\r', '').strip()
        component = td2.get_text('|').replace('\r', '').strip()
        cps = component.replace('| x', '').replace('zenny', ' zenny').split('|')
        slot = 1
        aus = augment.split('|')
        name = aus[0]
        nums = re.findall("\d+", augment)
        # print('augment', augment)
        # print('cps', cps)
        lv = 1
        if nums:
          lv = nums[0]
          if 'Slot' in augment:
            slot = nums[1]
        for v in cps:
          v = v.strip()
          vs = v.split()
          if len(vs) != 2:
            continue
          if 'zenny' in v:
            zn = vs[0].replace(',', '')
            srr.append("('{}', {}, {}, '{}', '{}', {}, '{}')".format('金币', zn, lv, name, sm, slot, wpName))
          else:
            srr.append("('{}', {}, {}, '{}', '{}', {}, '{}')".format(vs[0], vs[1], lv, name, sm, slot, wpName))
        # print('='*11)
        # print('1',augment)
        # print('2',sm)
        # print('3',component)
      sql += ','.join(srr)
      sqls.append(sql)
    elif '语言' in tn:
      name_hk = trs[7].select('td')[0].get_text().strip()
    print('='*88)
  return [rarity, element, tree_en, elderseal, weapon_type, name_hk, cust,unlock,skill, preWeapon,'|'.join(toWeapons), desc, ','.join(music), gunType, gunLv, shake]

# getItem('https://mhw.poedb.tw/chs/weapon/Bone%20Blade%20II')
# getItem('https://mhw.poedb.tw/chs/weapon/Ruinous%20Atrocity')
# getItem('https://mhw.poedb.tw/chs/weapon/Empress%20Galea')
# getItem('https://mhw.poedb.tw/chs/weapon/Emperor%20Thundersword')
# wp = getItem('https://mhw.poedb.tw/chs/weapon/Empress%20Galea%20%22Ruin%22')
# wp = getItem('https://mhw.poedb.tw/chs/weapon/Tiger%20Jawblade')
# ["骨剑3", "https://mhw.poedb.tw/chs/weapon/Bone%20Blade%20III", "576", "", "", [], [[["danger", 90], ["warning", 50], ["yellow", 50], ["success", 10], ["dark", 200]], [["danger", 90], ["warning", 50], ["yellow", 50], ["success", 60], ["dark", 150]]]]
'''
TRUNCATE t_weapon;
TRUNCATE t_wp_craft;
TRUNCATE t_wp_custom;
SELECT DISTINCT tree FROM t_weapon WHERE type = 242 and tree != ''
-- delete FROM t_weapon WHERE type = 250
select * FROM t_weapon WHERE type = 244 order by id
'''
# 愤怒双刃 数据纠正 [100:105]
# 破坏歼灭之刚弓、断灭崩坏之刚烈弓
wpType = 252
nameArr = []
with open(r'D:\git_pro\note\mhw\3_weapon\sql\252.json', 'r', encoding='utf-8') as inf:
  for il in inf.readlines():
    jd = json.loads(il)
    [name, url, attack, affinity, defense, slots, whets] = jd
    if not defense:
      defense = 0
    slotStr = ','.join(slots)
    # arr = []
    # for rows in whets:
    #   brr = []
    #   for wh in rows:
    #     aw = wh[0]+':'+str(wh[1])
    #     brr.append(aw)
    #   arr.append(','.join(brr))
    # whet = '|'.join(arr)
    whet = whets
    wp = getItem(url, name)
    [rarity, element, tree_en, elderseal, weapon_type, name_hk, cust,unlock,skill, pre,to,desc, music, gunType, gunLv, shake] = wp
    key = name+rarity
    if not key in nameArr:
      sq = "insert into t_weapon values (null,'{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}',{})".format(name,tree_en,pre,to,rarity,attack,defense,affinity,element,elderseal,slotStr,desc,whet,unlock,skill,wpType,name_hk,cust,music,gunType,gunLv)
      wps.append(sq)
    else:
      print('key', key, url)
    time.sleep(2)
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\252.sql', 'w', encoding='utf-8') as out:
    for line in sqls:
      out.write(line+';\n')
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\252_wp.sql', 'w', encoding='utf-8') as out:
    for line in wps:
      out.write(line+';\n')
