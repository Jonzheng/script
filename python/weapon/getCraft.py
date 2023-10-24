import requests, json, sys, time
from bs4 import BeautifulSoup
sqls = []
sqls2 = []
wps = []
def getItem(url, wpName):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  preWeapon = ''
  for cd in cards:
    tn = ''
    head = cd.select('.card-header')
    hasImg = []
    if head:
      tn = head[0].get_text().strip()
      hasImg = head[0].select('img')
    tb = cd.select('table')[0]
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('@', tn, '-', th)
    if 'Crafting' in tn:
      for tr in trs:
        tds = tr.select('td')
        if len(tds) == 0:
          continue
        [td1, td2] = tds
        create = 0
        preWeapon = ''
        sql = ''
        unlock = ''
        zenny = 0
        type = td1.get_text().strip()
        if '强化' in type:
          preWeapon = td1.select('a')[0].get_text().strip()
        elif 'Create' in type:
          create = 1
        component = td2.get_text('|').replace('\r', '').strip().replace('| x', '')
        # print(create, component)
        if create == 1 or preWeapon:
          # insert into t_wp_craft values ('foo', 1),('bar', 2);
          # component 80000 zenny|歼灭的大刚角| x 3|灭尽龙的刚爪| x 4|无穷的新生壳| x 5|古龙的大宝玉| x 1|Unlock: |歼世灭尽龙
          cps = component.replace('| x', '').replace('Unlock: |', 'Unlock:').split('|')
          srr = []
          for v in cps:
            v = v.strip()
            vs = v.split()
            # print(len(vs), vs)
            if 'Unlock' in v:
              unlock = v.replace('Unlock:', '')
            if len(vs) == 1:
              continue
            if 'zenny' in v:
              zenny = vs[0].replace(',', '')
            else:
              srr.append("{}:{}".format(vs[0], vs[1]))
          sql = "insert into t_wp_craft values ('{}', '{}', '{}', {}, {})".format(wpName, '|'.join(srr), unlock, zenny, create)
          sqls.append(sql)
    # elif len(hasImg) > 0:
    #     for tr in trs:
    #       th1 = tr.select('th')[0].get_text().strip()
    #       td1 = tr.select('td')[0].get_text().strip()
    #       if 'element' in th1:
    #         element = td1.replace('paralysis', 'paralysis:').replace('thunder', ' thunder:').replace('sleep', ' sleep:')
    #         element = element.replace('blast', ' blast:').replace('ice', ' ice:').replace('water', ' water:')
    #         element = element.replace('fire', ' fire:').replace('dragon', ' dragon:').replace('poison', ' poison:')
    #         if '(' in element:
    #           element = element.replace('(', '').replace(')', '')
    #           element = element.replace(':', ':(') + ')'
    #         element = element.strip()
    #         ss = "update t_weapon set `element` = '{}' where name = '{}'".format(element, wpName)
    #         sqls2.append(ss)


# getItem('https://mhw.poedb.tw/chs/weapon/Chrome%20Deathscythe%20II', '铬钢死神镰刀2')
# getItem('https://mhw.poedb.tw/chs/weapon/Chrome%20Deathscythe%20I', '铬钢死神镰刀1')


with open(r'D:\git_pro\note\mhw\3_weapon\sql\246.json', 'r', encoding='utf-8') as inf:
  for il in inf.readlines():
    jd = json.loads(il)
    [name, url, attack, affinity, defense, slots, whets] = jd
    if '铠罗' in name or '金色的' in name or '赤龙' in name or '皇金' in name:
      continue
    wp = getItem(url, name)
    time.sleep(1)
  with open(r'D:\git_pro\note\mhw\3_weapon\sql\craft\246_craft.sql', 'w', encoding='utf-8') as out:
    for line in sqls:
      out.write(line+';\n')
  # with open(r'D:\git_pro\note\mhw\3_weapon\sql\craft\246_up.sql', 'w', encoding='utf-8') as out:
  #   for line in sqls2:
  #     out.write(line+';\n')

