import requests, time


for i in range(0, 256):
  link = 'https://mhw.poedb.tw/images/cmn_item00/{}.png'.format(i)
  # link = 'https://mhw.poedb.tw/images/color/{}.png'.format(i)
  # link = 'https://mhw.poedb.tw/images/icon/{}.png'.format(i)
  print(link)
  resp = requests.get(link)
  if resp.status_code == 200:
    fna = link.split('/')[-1] # 22_8.png
    with open('D:/git_pro/note/mhw/icon4/'+ fna, 'wb') as out:
      out.write(resp.content)
  else:
    print(resp.status_code)
  time.sleep(1)