import json
from bs4 import BeautifulSoup, element

ff1 = r'D:\git_me\script\python\skill\data\list.html'
ff2 = r'D:\git_me\script\python\skill\data\list.json'

drr = []
crr = []
with open(ff1, 'r', encoding='utf-8') as inf:
  tt = inf.read()
  soup = BeautifulSoup(tt, 'lxml')
  trs = soup.find_all(name='tr')
  for tr in trs:
    tds = tr.select('td')
    if len(tds) > 1:
      td1 = tds[1]
      aa = td1.select('a')[0]
      link = aa['href']
      if link not in drr:
        drr.append(link)
        name = aa.string.replace('すりんがーそうてんすうあっぷ', '投射器装填数提升').replace('きんじしのどき', '金狮子的怒气')
        name = name.replace('どうりょくげん', '蓄电池').replace('さばいばー', '生还者')
        name = name.replace('まんぷくのしゅくふく', '万福的祝福').replace('せきりゅうのふういん', '冥赤龙的封印')
        name = name.replace('だいかんしゃのしゅくふく', '大感谢的祝福').replace('まんかいのしゅくふく', '盛放之祝福')
        name = name.replace('じょうねつのしゅくふく', '热情的祝福').replace('ほらーないとのしゅくふく', '惊魂夜的祝福')
        name = name.replace('きんじしのとうし', '金狮子的斗志').replace('さいりゅうのとうし', '碎龙之斗志')
        name = name.replace('らんきりゅうのしんずい', '绚辉龙的真髓').replace('ひょうがりゅうのぜつぎ', '冰牙龙的绝技')
        name = name.replace('こうこくりゅう的しんぴ', '煌黑龙的神秘')
        name = name.replace('にゅーわーるど', '新世界')
        print(name, link)
        crr.append([name, link])
print(len(crr))

with open(ff2, 'w', encoding='utf-8') as out:
  out.writelines(json.dumps(crr, ensure_ascii=False))