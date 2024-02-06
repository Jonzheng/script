from bs4 import BeautifulSoup

ff1 = r'D:\git_me\script\python\weapon\data\update251music.html'
ff2 = r'D:\git_me\script\python\weapon\sql\update_251.sql'

with open(ff2, 'w', encoding='utf-8') as out:
  with open(ff1, 'r', encoding='utf-8') as inf:
    tt = inf.read()
    soup = BeautifulSoup(tt, 'lxml')
    trs = soup.find_all(name='tr')
    for tr in trs:
      tds = tr.select('td')
      if len(tds) > 4:
        [td1, td2, td3, td4, td5] = tds
        name = td1.select('a')[0].get_text().strip()
        music = td4.get_text('|').replace('\r', '').replace('\n', '').strip()
        music = music.replace('||||||||||||||||||||||||','').replace('|||||||||||||||||||||||','').replace('||||||||||||||||||||||','').strip('|')
        arr = music.split('|')
        if len(arr) > 1:
          music = arr[1]
          print(name, music, arr)
        sql = "update t_weapon set music = '{}' where name = '{}';\n".format(music, name)
        out.write(sql)

