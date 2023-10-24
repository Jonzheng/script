import json

with open(r'D:\git_pro\note\mhw\1reward\rere.json', 'r', encoding='utf-8') as inf:
    dd = json.loads(inf.read())
    for it in dd:
      if len(it) > 2:
        print('-', it[0], it[1])
        for dc in it[2:]:
          print(dc)