import time, json, requests, sys
from bs4 import BeautifulSoup
msql = []
def getItem(url):
  suf = url.split('/')[-1]
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  cards = soup.select('.card')
  limp = ''
  capture = ''
  stage = ''
  name = ''
  name_jp = ''
  name_en = ''
  threat = ''
  note = ''
  info = ''
  desc = ''
  rank = ''
  basehp = ''
  cate = ''
  for cd in cards:
    tn = cd.select('.card-header')[0].get_text().strip()
    tb = cd.select('table')[0]
    print('@', tn)
    th0 = tb.select('th')[0]
    trs = tb.select('tr')
    th = th0.get_text().strip()
    print('th:', th)
    if suf in tn:
      for tr in trs:
        th1 = tr.select('th')[0].get_text().strip()
        td1 = tr.select('td')[0].get_text().strip()
        if th1 == '等级':
          rank = td1.replace('Master', '大师').replace('Rank', '').strip()
        elif th1 == '危险度':
          threat = td1
        elif th1 == 'Limp':
          limp = td1
        elif th1 == '捕获%s':
          capture = td1
        elif th1 == 'Base HP':
          basehp = td1
        elif th1 == '生态信息':
          cate = td1
        elif th1 == '主要栖息地':
          stage = td1
          if stage.endswith(','):
            stage = stage[:-1]
        elif th1 == '调查员的笔记':
          note = td1.replace('\n', '').replace('\r', '').strip()
        elif th1 == '对狩猎有用的信息':
          info = td1.replace('\n', '').replace('\r', '').strip()
        elif th1 == 'Description':
          desc = td1.replace('\n', '').replace('\r', '').strip()
    if '语言' in tn:
      name_jp = trs[0].select('td')[0].get_text().strip()
      name_en = trs[1].select('td')[0].get_text().replace('\'', '·').strip()
      name = trs[8].select('td')[0].get_text().strip()
    print('='*88)
  print('==', name, name_jp, name_en)
  print('=', rank, limp, cate)
  sql = "insert into t_monster (name, `rank`, cate, `threat`, capture, limp, basehp, stage, name_jp, name_en, note, info, `desc`) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');\n".format(name, rank, cate, threat, capture, limp, basehp, stage, name_jp, name_en, note, info, desc)
  return sql

# links = r'D:\git_pro\note\mhw\0_monsters\mon_link.json'
# count = 0
# with open(r'D:\git_pro\note\mhw\0_monsters\monsql\t_mon2.sql', 'w', encoding='utf-8') as out:
#   with open(links, 'r', encoding='utf-8') as inf:
#       dd = json.loads(inf.read())
#       for line in lrr:
#           print(line)
#           count += 1
#           ol = getItem(line[1])
#           out.write(ol)
#           time.sleep(1)

lrr = ['https://mhw.poedb.tw/chs/monster/Anjanath', 'https://mhw.poedb.tw/chs/monster/Tzitzi-Ya-Ku']
with open(r'D:\git_pro\note\mhw\0_monsters\monsql\t_mon2.sql', 'w', encoding='utf-8') as out:
  for url in lrr:
    print(url)
    ol = getItem(url)
    out.write(ol)
    time.sleep(1)