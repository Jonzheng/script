import requests, json, time
from bs4 import BeautifulSoup
rarity = '5'
detail = {}
bakArr = []
sqls = []
def getItem(url):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  skill = ''
  craft = ''
  icon = ''
  slots = []
  lvArr = []
  for cd in cards:
    tn = ''
    head = cd.select('.card-header')
    ctext = cd.select('.card-text')
    if ctext:
      desc = ctext[0].get_text().replace('\r', '').replace('\n', '').strip()
    if head:
      tn = head[0].get_text().strip()
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if 'Defense' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        slots = []
        [td1, td2, td3, td4, td5, td6, td7,td8, td9, td10] = tds
        icon = td1.select('img')[0]['style'].split('/')[-1].split('.')[0]
        name = td2.get_text().strip()
        defence = td3.get_text().replace('&dash;', '-').strip()
        defence = defence.replace(' - ', '-').replace(' (', '|').replace(')', '')
        fire = td4.get_text().strip()
        water = td5.get_text().strip()
        thunder = td6.get_text().strip()
        ice = td7.get_text().strip()
        dragon = td8.get_text().strip()
        imgs = td9.select('img')
        if len(imgs) > 0:
          for img in imgs:
            slot = img['style'].split('/')[-1].split('.')[0]
            slot = slot.replace('67', '2').replace('68', '3').replace('69', '3').replace('73', '4').replace('66', '1').replace('72', '4')
            slots.append(slot)
        skill = td10.get_text('|').replace('|+', ':').replace(' |', '|').strip()
        detail[name] = [icon, defence, fire, water, thunder, ice, dragon, ','.join(slots), skill]
        # stage = td2.get_text().strip()
        # star = td3.get_text().strip()
    elif 'Level' in th:
      skiCate = tn.split('/')[0].strip()
      skiCate = skiCate.replace('すりんがーそうてんすうあっぷ', '投射器装填数提升').replace('きんじしのどき', '金狮子的怒气')
      skiCate = skiCate.replace('どうりょくげん', '蓄电池').replace('さばいばー', '生还者')
      skiCate = skiCate.replace('まんぷくのしゅくふく', '万福的祝福').replace('せきりゅうのふういん', '冥赤龙的封印')
      skiCate = skiCate.replace('だいかんしゃのしゅくふく', '大感谢的祝福').replace('まんかいのしゅくふく', '盛放之祝福')
      skiCate = skiCate.replace('じょうねつのしゅくふく', '热情的祝福').replace('ほらーないとのしゅくふく', '惊魂夜的祝福')
      skiCate = skiCate.replace('きんじしのとうし', '金狮子的斗志').replace('さいりゅうのとうし', '碎龙之斗志')
      skiCate = skiCate.replace('らんきりゅうのしんずい', '绚辉龙的真髓').replace('ひょうがりゅうのぜつぎ', '冰牙龙的绝技')
      skiCate = skiCate.replace('こうこくりゅう的しんぴ', '煌黑龙的神秘')
      skiCate = skiCate.replace('にゅーわーるど', '新世界')
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 3:
          [td1, td2, td3] = tds
          lv = td1.get_text().strip()
          desc2 = td2.get_text(':').replace('\r', '').replace('\n', '').strip()
          desc2 = desc2.replace(':（', '（')
          # params = td3.get_text().strip()
          # print(lv, ':', params)
          # print('desc2', desc2)
          # lvArr.append(';'.join([lv, desc2, params]))
          skName = desc2.split(':')[0].strip()
          lvArr.append(':'.join([skiCate,lv,skName]))
    elif 'Crafting' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        [td1, td2] = tds
        name = td1.get_text().strip()
        component = td2.get_text('|').replace('\r', '').strip().replace('| x', '')
        cps = component.split('|')
        srr = []
        for v in cps:
          v = v.strip()
          vs = v.split()
          if len(vs) > 1:
            srr.append("{}:{}".format(vs[0], vs[1]))
        craft = '|'.join(srr).replace('\'', '.')
        # print('name', name)
        # print('craft', craft)
        # print('lvArr', '|'.join(lvArr))
        # print('detail', detail[name])
        if '【' not in name:
          [icon, defence, fire, water, thunder, ice, dragon, slot, skill] = detail[name]
          suits = '|'.join(lvArr)
          icon = int(icon) + 1
          sql = "update t_armor set slot = '{}' where name = '{}';".format(slot, name)
          sqls.append(sql)
        elif detail[name]:
          detail[name].extend([name, '|'.join(lvArr), craft])
          bakArr.append(detail[name])
        else:
          print('detail nil', name)


names = []
print('⭐⭐⭐⭐⭐⭐⭐⭐⭐', rarity)
with open(r'D:\git_me\script\python\armor\data\list'+rarity+'.json', 'r', encoding='utf-8') as inf:
  list = json.loads(inf.readlines()[0])
  for arr in list:
    print('arr', arr)
    [name, url] = arr
    url = 'https://mhw.poedb.tw' + url
    chm = getItem(url)
    time.sleep(2)
  with open(r'D:\git_me\script\python\armor\data\t_upslot_armor'+rarity+'.sql', 'w', encoding='utf-8') as out:
    for sql in sqls:
      out.write(sql+';\n')
  with open(r'D:\git_me\script\python\armor\data\t_bak'+rarity+'.js', 'w', encoding='utf-8') as out:
    for sql in bakArr:
      out.write(json.dumps(sql, ensure_ascii=False)+';\n')


