
mp = {}
kv = {
        'Tail': '尾部',
        'Shell': '壳',
        'Magma Core': '热核',
        'Weak Shells': '软壳',
        'Hindlegs': '后肢',
        'Chest': '胸部',
        'Forelegs': '前肢',
        'Body': '身体',
        'Charged': '带电',
        'Tail Tip': '尾尖',
        'Head': '头部',
        'Legs': '腿部',
        'Wings': '翅膀',
        'Belly': '腹部',
        'Ears': '耳朵',
        'Mane': '鬃毛',
        'Broken': '破坏',
        'Stomach': '胃',
        'Neck': '颈部',
        'Bottom': '底部',
        'Top': '顶部',
        'Upper Neck': '上颈部',
        'Upper Neck': '下颈部',
        'Jaw': '下颚',
        'Antennae': '触角',
        'Molten': '熔岩',
        'Released': '释放',
        'Crater': '火山口',
        'Back': '背部',
        'Central': '中央',
        'Rear': '后背',
        'Critical': '重伤',
        'Hind Legs': '后肢',
        'Tail Base': '尾座',
        'Hvy Crystal': '重水晶',
        'Sharpened': '锐化',
        'Throat': '喉咙',
        'Arms': '手臂',
        'Fire': '火',
        'Ice': '冰',
        'Dragon': '龙',
        'Nose': '鼻子',
        'Horns': '角',
        'Horn': '角',
        'Forearms': '前臂',
        'Neck/Back': '颈/背',
        'Claws': '爪',
        'Front Legs': '前腿',
        'Mud': '泥',
        'Shoulder': '肩膀',
        'Snow': '雪甲',
        'Body/Back': '身体/背',
        'Spore Sac': '孢子囊',
        'Enraged': '怒',
        'Enraged': '角',
        'Rock 1': '岩1',
        'Rock 2': '岩2',
        'Front Legs': '前腿',
        'Rampage': '狂暴',
        'Rusted': '生锈',
        'Heating': '加热',
        'Inflated': '充气',
        'Fins': '鳍片',
        'Electric': '带电',
        'Lower Body': '下身体',
        'Rock': '抱岩',
        'Exp. Foreleg': 'Exp.前肢',
        'Hardened': '硬化',
        'Abdomen': '腹部',
        'Heated': '热的',
        'Dehydrated': '脱水',
        'White': '白',
        'Black': '黑',
        'Neck Pouch': '颈袋',
        'Tongue': '舌头',
        'Head Bone': '头骨',
        'Back Bone': '背骨',
        'Leg Bone': '腿骨',
        'Red Slime': '红',
        'S. Critical': 'S.伤',
        'Upper Tail': '上尾部',
        'B.S. Critical': 'B.S.伤',
        'Forefeet': '前足',
        'Foreleg+Feet': '前腿+足',
        'Hindleg+Feet': '后腿+足',
        'Hindfeet': '后足',
        'Wing Tips': '翼尖',
        'Webbing': '织带',
        'Torso': '躯干',
        'Snout': '鼻子',
        'Head Casing': '头壳',
        'Body/Legs': '身体/腿',
        'Lower Neck': '下颈',
    }
with open(r'D:\git_pro\note\mhw\0_monsters\monid.txt', 'r', encoding='utf-8') as inf:
    for le in inf.readlines():
        [id, name, en] = le.strip().split(';')
        mp[en.lower()] = name

with open(r'D:\git_pro\note\mhw\2weak\t_weakness.sql', 'w', encoding='utf-8') as out:
    with open(r'D:\git_pro\note\mhw\2weak\weak1.tsv', 'r', encoding='utf-8') as inf:
        for lne in inf.readlines():
            arr = lne.split('\t')
            # print(len(arr), arr)
            [idx, en, ke, part, state, hue, ham, far, fire, water, thunder, ice, dragon,a,s,d,f,g,h,j ] = arr
            en = en.strip()
            part = part.strip()
            state = state.strip()
            if en and not mp.get(en.lower()):
                continue
            # print(en, mp.get(en.lower()))
            name = mp.get(en.lower())
            part = kv.get(part)
            state = kv.get(state)
            sql = "insert into t_weakness (monster_name, part, `state`, hue, ham, far, fire, water, thunder, ice, dragon) values('{}','{}','{}',{},{},{},{},{},{},{},{});\n".format(name,part,state, hue, ham, far, fire, water, thunder, ice, dragon)
            out.write(sql)
