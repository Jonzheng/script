import time, json, requests
from bs4 import BeautifulSoup

def getItem(url):
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.element-wrapper')
  monster_name = soup.select('.project-title')[0].get_text().strip()
  sqls = []
  for cd in cards:
    tn = cd.select('.element-header')[0].get_text().strip()
    print('@', tn)
    cl4s = cd.select('.col-lg-4')
    for cl4 in cl4s:
      rank = cl4.select('h6')[0].get_text().strip()
      crr = [tn, rank]
      tbs = cl4.select('tbody')
      condit = ''
      slot = 0
      for tb in tbs:
        trs = tb.select('tr')
        tbrr = []
        for tr in trs:
          tdrr = []
          tds = tr.select('td')
          for td in tds:
            ss = td.get_text().replace('\s', '').replace('\n', '').replace('\r', '').replace(' ', '').strip()
            if len(tds) == 1:
              condit = ss
              slot += 1
            else:
              tdrr.append(ss)
          if len(tdrr) > 1:
            tdrr.append(condit)
            tdrr.append(slot)
            tbrr.append(tdrr)
        crr.append(tbrr)
        for ol in tbrr:
          [item_name, prec, condit, slot] = ol
          sp = item_name.split('×')
          item_name = sp[0]
          quantity = 1
          if len(sp) > 1:
            quantity = sp[1]
          prec = prec.split('%')[0]
          condit = condit.replace('GuidingLands', '引导之地').replace('Low', '低').replace('Mid', '中').replace('High', '高').replace('Tempered', '历战')
          condit = condit.replace('InvestigationReward', '调查奖励')
          condit = condit.replace('Silver', '银').replace('Gold', '金').replace('Bronze', '铜').replace('Purple', '紫')
          # print(rank, monster_name, condit, slot, item_name, quantity, prec)
          # lines.append([rank, monster_name, condit, slot, item_name, quantity, prec])
          sql = "insert into t_reward (`rank`, monster_name, item_name, slot, condit, quantity, `prec`) values('{}','{}','{}',{},'{}',{}, {});\n".format(rank, monster_name, item_name,slot, condit, quantity, prec)
          sqls.append(sql)
  return sqls

links = r'D:\git_pro\note\mhw\0_monsters\mon_link2.json'
with open(r'D:/git_pro/note/mhw/1reward/t_reward71.sql', 'w', encoding='utf-8') as out:
  with open(links, 'r', encoding='utf-8') as inf:
      dd = json.loads(inf.read())
      for line in dd[20:]:
          print(line)
          sqls = getItem(line[1])
          for ol in sqls:
            out.write(ol)
          time.sleep(1)