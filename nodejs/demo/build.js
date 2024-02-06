const { mysql, encry } = require('../util/conf')
const { getSkill } = require('./skill')

exports = module.exports = {
  queryArr: async (ctx) => {
    const { query } = ctx.request
    const buildArr = await mysql('t_build')
    encryData = encry(JSON.stringify({ buildArr }))
    ctx.body = encryData
  },
  queryOne: async (ctx) => {
    const { query } = ctx.request
    const { id } = query
    const [id0, id1, id2, id3, id4 ,id5, id6, id7 ,id8] = '2003:390:397:|192:3:36:37|193:156:157:8|194:290:71:|195::31:|196::35:54|33|2:76:76|4:92:92'.split('|')

    const [w0, w1, w2, w3] = id0.split(':')
    const [weapon] = await mysql('t_weapon').select('id', 'name', 'slot', 'rarity', 'type as icon', 'skill', 'affinity').where('id', w0)
    if (weapon && weapon.skill) {
      weapon.skiArr = await Promise.all(weapon.skill.split('|').map(async sks => {
        return getSkill(sks);
      }));
    }
    const [wd1] = await mysql('t_decor').where('id', w1);
    const [wd2] = await mysql('t_decor').where('id', w2);
    const [wd3] = await mysql('t_decor').where('id', w3);
    const wds = [wd1, wd2, wd3]
    if (weapon.slot) {
      weapon.slot = await Promise.all(weapon.slot.split(',').map(async (slot, idx) => {
        let id = ''
        let name = ''
        let sloted = ''
        let color = ''
        let skill = ''
        if (wds[idx]) {
          id = wds[idx].id
          name = wds[idx].name
          sloted = wds[idx].slot
          color = wds[idx].color
          skill = wds[idx].skill
        }
        let skiArr = [];
        if (skill) {
          skiArr = await Promise.all(skill.split('|').map(async sks => {
            return getSkill(sks);
          }));
        }
        return { id, slot, name, sloted, color, skill, skiArr }
      }))
    }

    const armorArr = await Promise.all([id1, id2, id3, id4 ,id5].map(async asp => {
      const [b0, b1, b2, b3] = asp.split(':')
      const [armor] = await mysql('t_armor').select('id', 'name', 'slot', 'rarity', 'icon', 'skill', 'suits').where('id', b0);
      const [decor1] = await mysql('t_decor').where('id', b1);
      const [decor2] = await mysql('t_decor').where('id', b2);
      const [decor3] = await mysql('t_decor').where('id', b3);
      const des = [decor1, decor2, decor3]
      if (armor && armor.skill) {
        armor.skiArr = await Promise.all(armor.skill.split('|').map(async sks => {
          return getSkill(sks);
        }));
      }

      if (armor.slot) {
        armor.slot = await Promise.all(armor.slot.split(',').map(async (slot, idx) => {
          let id = ''
          let name = ''
          let sloted = ''
          let color = ''
          let skill = ''
          if (des[idx]) {
            id = des[idx].id
            name = des[idx].name
            sloted = des[idx].slot
            color = des[idx].color
            skill = des[idx].skill
          }
          let skiArr = [];
          if (skill) {
            skiArr = await Promise.all(skill.split('|').map(async sks => {
              return getSkill(sks);
            }));
          }
          return { id, slot, name, sloted, color, skill, skiArr }
        }))
      }

      if (armor.suits) {
        armor.suitArr = await Promise.all(armor.suits.split('|').map(async sks => {
          const [parent, lv, skName] = sks.split(':')
          armor.suitName = parent
          const { id = 1 } = await getSkill(sks);
          armor.suitId = id;
          return { lv, skName }
        }))
      }

      return armor;
    }));

    const [charm] = await mysql('t_charm').where('id', id6);

    if (charm && charm.skill) {
      charm.skiArr = [];
      charm.skill.split('|').forEach(async sks => {
        const sk = await getSkill(sks);
        charm.skiArr.push(sk);
      });
    }
    if (charm) {
      charm.icon = 230;
    }
    const cloakArr = await Promise.all([id7, id8].map(async asp => {
      const [b0, b1, b2] = asp.split(':')
      const [cloak] = await mysql('t_cloak').select('id', 'name', 'slot', 'icon', 'color', 'maxed').where('id', b0);
      const [decor1] = await mysql('t_decor').where('id', b1);
      const [decor2] = await mysql('t_decor').where('id', b2);
      const des = [decor1, decor2]
      if (cloak.slot) {
        cloak.slot = await Promise.all(cloak.slot.split(',').map(async (slot, idx) => {
          let id = ''
          let name = ''
          let sloted = ''
          let color = ''
          let skill = ''
          if (des[idx]) {
            id = des[idx].id
            name = des[idx].name
            sloted = des[idx].slot
            color = des[idx].color
            skill = des[idx].skill
          }
          let skiArr = [];
          if (skill) {
            skiArr = await Promise.all(skill.split('|').map(async sks => {
              return getSkill(sks);
            }));
          }
          return { id, slot, name, sloted, color, skill, skiArr }
        }))
      }

      return cloak;
    }));

    encryData = encry(JSON.stringify({ build: [weapon, ...armorArr, charm, ...cloakArr] }))
    ctx.body = encryData
  },
  saveOne: async (ctx) => {
    const { body } = ctx.request
    const { userId, type, gear, slot, skied, cust, skirr, armor, tag, desc, creator } = body

    const [build] = await mysql('t_build').select('id', 'skied', 'cust').where({'uid': userId, 'type': type, 'gear': gear, 'slot': slot}).orderBy('id', 'desc');
    if (build && build.skied == skied && build.cust == cust){
      return ctx.body = {code: 201, msg: '无法新增重复配装'}
    }

    await mysql('t_build').insert({'uid': userId, gear, slot, type, skied, cust, skirr, armor, tag, desc, creator});
    ctx.body = {code: 200, msg: 'ok'}

  }
}