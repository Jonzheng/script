

arr = ['攻击力强化5','攻击力强化6','会心率强化5','会心率强化6','属性强化5','属性强化6','防御力强化5','防御力强化6','镶嵌槽强化3','镶嵌槽强化4','锐利度强化5','锐利度强化6']

brr = arr.map((it, idx) => {
  return { val: it, type: idx % 2 == 0 ? 0: 1,icon: 'up-att' }
})
console.log(JSON.stringify(brr))

