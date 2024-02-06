from bs4 import BeautifulSoup

ff1 = r'D:\git_me\script\python\food\foodSkill.html'
ff2 = r'D:\git_me\script\python\food\fdSki.sql'

with open(ff2, 'w', encoding='utf-8') as out:
  with open(ff1, 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 3:
        [td1, td2, td3, td4] = tds
        sty = td1.select('img')[0]['style']
        color = sty.split(';')[0].split('/')[-1].split('.')[0]
        name = td1.get_text().strip()
        desc = td2.get_text().replace('\n', '').replace('  ', '').strip()
        ski = td3.get_text().strip()
        qtity = td4.get_text().strip()
        sql = "insert into t_fd_skill values (null, {},'{}', '{}', '{}', {});".format(color, name, desc, ski, qtity)
        out.write(sql + '\n')


