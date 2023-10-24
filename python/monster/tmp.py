import requests
from bs4 import BeautifulSoup

# resp = requests.get('https://mhw.poedb.tw/chs/monster/Jyuratodus')
# soup = BeautifulSoup(resp.text, 'lxml')

# with open(r'D:\git_pro\note\mhw\html0\Jyuratodus.html', 'w', encoding='utf-8') as out:
#   cards = soup.select('.card')
#   for c in cards:
#     out.write(str(c)+'\n')

msql = []
name_en = ''
with open(r'D:\git_pro\note\mhw\html0\Jyuratodus.html', 'r', encoding='utf-8') as inf:
    soup = BeautifulSoup(inf.read(), 'lxml')
    cards = soup.select('.card')
    wnArr = []
    staArr = []
    dmgArr = []
    rwdArr = []
    bkArr = []
    egArr = []
    mrr = []
    hrr = []
    lrr = []
    for cd in cards:
      tn = cd.select('.card-header')[0].get_text().strip()
      tb = cd.select('table')[0]
      print('-'*66)
      print('@', tn)
      print('--')
      th0 = tb.select('th')[0]
      trs = tb.select('tr')
      th = th0.get_text().strip()
      print('th:', th)
      if th == '等级':
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
          elif th1 == '调查员的笔记':
            note = td1.replace('\n', '')
          elif th1 == '对狩猎有用的信息':
            info = td1.replace('\n', '')
          elif th1 == 'Description':
            desc = td1.replace('\n', '')
      if 'Weakness' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          brr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            brr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            brr.append(val)
          wnArr.append(brr)
      if 'Status' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          crr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            crr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            crr.append(val)
          staArr.append(crr)
      if 'Damage' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          drr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            drr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            drr.append(val)
          dmgArr.append(drr)
      if 'Rewards' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          trr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            trr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            trr.append(val)
          rwdArr.append(trr)
          if 'Master' in tn:
            mrr.append(trr)
          elif '上位' in tn:
            hrr.append(trr)
          elif '下位' in tn:
            lrr.append(trr)
      if '破坏部位' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          frr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            frr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            frr.append(val)
          bkArr.append(frr)
      if 'Enrage' in tn:
        for tr in trs:
          th3s = tr.select('th')
          td2s = tr.select('td')
          krr = []
          for i, val in enumerate(th3s):
            val = val.get_text().strip()
            krr.append(val)
          for i, val in enumerate(td2s):
            val = val.get_text().strip()
            krr.append(val)
          egArr.append(krr)
      if '语言' in tn:
        name_jp = trs[0].select('td')[0].get_text().strip()
        name_en = trs[1].select('td')[0].get_text().replace('\'', '·').strip()
        name = trs[8].select('td')[0].get_text().strip()
      print('='*88)
    # print('wnArr', wnArr)
    # print('staArr', staArr)
    # print('dmgArr', dmgArr)
    # print('rwdArr', rwdArr)
    # print('bkArr', bkArr)
    # print('egArr', egArr)
    print('==', name, name_jp, name_en)
    print('=', rank, limp, cate)

    print('=', note, info, desc)
    sql = "insert into t_monster (name, `rank`, cate, `threat`, capture, limp, basehp, stage, name_jp, name_en, note, info, `desc`) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');\n".format(name, rank, cate, threat, capture, limp, basehp, stage, name_jp, name_en, note, info, desc)
    msql.append(sql)
    for it in mrr[1:]:
      [condit, sp, prec] = it
      condit = condit.replace('Track', '怪物痕迹').replace('Shiny Drop', '掉落物').replace('Palico Bonus', '随从采集物')
      condit = condit.replace('The Guiding Lands', '引导之地').replace('Low', '低').replace('Mid', '中').replace('Tempered', '高')
      condit = condit.replace('%s的', '').replace('%s', '').replace('Investigation', '调查奖励')
      condit = condit.replace('Silver', '银').replace('Gold', '金').replace('Bronze', '铜').replace('Purple', '紫')
      item_name = sp.split('x')[0].strip()
      quantity = sp.split('x')[1]
      prec = prec.split("%")[0]
      sql = "insert into t_reward (`rank`, monster_name, condit, item_name, quantity, name_en, prec) values('大师','{}','{}','{}',{},'{}',{});\n".format(name, condit, item_name, quantity, name_en, prec)
      msql.append(sql)
    print('='*8)
    for it in hrr[1:]:
      [condit, sp, prec] = it
      condit = condit.replace('Track', '怪物痕迹').replace('Shiny Drop', '掉落物').replace('Palico Bonus', '随从采集物')
      condit = condit.replace('The Guiding Lands', '引导之地').replace('Low', '低').replace('Mid', '中').replace('Tempered', '高')
      condit = condit.replace('%s的', '').replace('%s', '').replace('Investigation', '调查奖励')
      condit = condit.replace('Silver', '银').replace('Gold', '金').replace('Bronze', '铜').replace('Purple', '紫')
      item_name = sp.split('x')[0].strip()
      quantity = sp.split('x')[1]
      prec = prec.split("%")[0]
      sql = "insert into t_reward (`rank`, monster_name, condit, item_name, quantity, name_en, prec) values('上位','{}','{}','{}',{},'{}',{});\n".format(name, condit, item_name, quantity, name_en, prec)
      msql.append(sql)
    print('='*8) 
    for it in lrr[1:]:
      [condit, sp, prec] = it
      condit = condit.replace('Track', '怪物痕迹').replace('Shiny Drop', '掉落物').replace('Palico Bonus', '随从采集物')
      condit = condit.replace('The Guiding Lands', '引导之地').replace('Low', '低').replace('Mid', '中').replace('Tempered', '高')
      condit = condit.replace('%s的', '').replace('%s', '').replace('Investigation', '调查奖励')
      condit = condit.replace('Silver', '银').replace('Gold', '金').replace('Bronze', '铜').replace('Purple', '紫')
      item_name = sp.split('x')[0].strip()
      quantity = sp.split('x')[1]
      prec = prec.split("%")[0]
      sql = "insert into t_reward (`rank`, monster_name, condit, item_name, quantity, name_en, prec) values('下位','{}','{}','{}',{},'{}',{});\n".format(name, condit, item_name, quantity, name_en, prec)
      msql.append(sql)

with open(r'D:\git_pro\note\mhw\html0\Jyuratodus.sql', 'w', encoding='utf-8') as out:
  for ol in msql:
    out.write(ol)