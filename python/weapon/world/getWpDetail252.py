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
  warr = []
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
          elif '偏移' in th1:
            music = [td1]
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

      sql += ','.join(srr)
      sqls.append(sql)
    elif '强化部位' in tn:
      for tr in trs:
        tds = tr.select('td')
        if not len(tds) == 4:
          continue
        [td1, td2, td3, td4] = tds
        shut = td1.get_text().strip()
        lv1 = list(filter(lambda x: not x == '-', td2.get_text(' ').split()))
        lv2 = list(filter(lambda x: not x == '-', td3.get_text(' ').split()))
        lv3 = list(filter(lambda x: not x == '-', td4.get_text(' ').split()))
        if td2.select('.rapid_fire'):
          lv1.insert(0, 'rep')
        else:
          lv1.insert(0, '-')
        if td3.select('.rapid_fire'):
          lv2.insert(0, 'rep')
        else:
          lv2.insert(0, '-')
        if td4.select('.rapid_fire'):
          lv3.insert(0, 'rep')
        else:
          lv3.insert(0, '-')
        whet = ';'.join([','.join(lv1), ','.join(lv2),','.join(lv3)])
        whet = whet.replace('Ex-Large', '特大').replace('Large', '大').replace('Big', '大').replace('Medium', '中').replace('Small', '小').replace('Auto', '自动')
        whet = whet.replace('Semi-slow', '稍微慢').replace('Normal', '普通').replace('Fast', '快').replace('Small', '小').replace('Slow', '慢')
        # print(shut + ':' + whet)
        warr.append(shut + ':' + whet)
    elif '语言' in tn:
      name_hk = trs[7].select('td')[0].get_text().strip()
    print('='*88)
  return [rarity, element, tree_en, elderseal, weapon_type, name_hk, cust,unlock,skill, preWeapon,'|'.join(toWeapons), desc, ','.join(music), gunType, gunLv, '|'.join(warr)]


wpType = 253
nameArr = []
with open(r'D:\git_pro\note\mhw\3_weapon\sql\253.json', 'r', encoding='utf-8') as inf:
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
    [rarity, element, tree_en, elderseal, weapon_type, name_hk, cust,unlock,skill, pre,to,desc, music, gunType, gunLv, warr] = wp
    whet = warr
    print('whet', len(whet))
    key = name+rarity
    if not key in nameArr:
      sq = "insert into t_weapon values (null,'{}','{}','{}','{}',{},{},{},'{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}',{})".format(name,tree_en,pre,to,rarity,attack,defense,affinity,element,elderseal,slotStr,desc,whet,unlock,skill,wpType,name_hk,cust,music,gunType,gunLv)
      wps.append(sq)
    else:
      print('key', key, url)
    time.sleep(2)
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\253.sql', 'w', encoding='utf-8') as out:
    for line in sqls:
      out.write(line+';\n')
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\253_wp.sql', 'w', encoding='utf-8') as out:
    for line in wps:
      out.write(line+';\n')
