arr = ['table', 'table-lightborder', 'table-sm', 22555, 'asdad', 'dddd', 'gfgg']
# print(arr, type(arr), 'table-lightborder' in arr)
from bs4 import BeautifulSoup, element
for s in arr:
    print(type(s), s, type(s) == 'str', isinstance(s, str))

print(element.Tag)

arr.append([123,23445])
# print(arr)
# ★1
import json
# ff1 = r'D:\git_pro\note\mhw\yan-que-shi.json'
# ff2 = r'D:\git_pro\note\mhw\links.json'
# with open(ff2, 'r', encoding='utf-8') as inf:
#     dd = json.loads(inf.read())
#     for line in dd:
#         print('=', line)
# print('lllllllllll', len(dd))

# ss = 'https://mhworld.kiranico.com/zh/items/evnne/ju-feng-de-bo-yu'
# drr = ss.split('/')
# print(drr[-2], drr[-1])
# ssl = 'insert into t_material (id, name, icon, desc, rarity, carry, buy, sell) values({},{})'.format(1,2)

# print(ssl)
# print(ssl.replace('(', "$"))

title = '大贼龙的鬃毛'
title2 = '水妖鸟的韧尾'

def getId(name):
    id = 0
    b2 = bytearray(name, encoding='gbk')
    cc = []
    for b in b2:
        cc.append(b)
    # print(len(b2), b2[1], name,len(name), len(cc), cc)
    n = 0
    id = ''
    while n < len(b2):
        pn = b2[n] + b2[n+1]
        while pn > 9:
            pn = pn >> 2
        id += str(pn)
        n += 2
    print(id, name)
    return id


# print('id1', getId(title), type(getId(title)))
# print('id2', getId(title2), type(getId(title2)))

its = ['？？？', '回复药','回复药·大','秘药','远古秘药','解毒药','汉方药','打消果实','元气饮料','携带食料','半生肉','烤熟的肉','烤焦的肉','冷饮','热饮','营养剂','营养剂·大','活力剂','星辰肉脯','强走药','怪力种子','鬼人药','鬼人药·大','怪力药丸','忍耐种子','硬化药','硬化药·大','忍耐的药丸','生命粉尘','生命大粉尘','汉方粉尘']

for it in its:
    print(it, getId(it))

crr = [1,2,3,4,5,6,7,8,9,10]

# icons = []
# with open(r'D:\git_pro\note\mhw\icons.json', 'w', encoding='utf-8') as out:
#     arr = ['22_0.png', '22_2.png']
#     out.writelines(json.dumps(arr))

# with open(r'D:\git_pro\note\mhw\icons.json', 'r', encoding='utf-8') as inf:
#    icons = json.loads(inf.read())


mp = {'ffds':123,'brk':456}

print("	Xeno'jiiva".replace('\'', '·').strip())

