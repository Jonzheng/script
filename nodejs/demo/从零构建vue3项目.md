
### 遇到的问题：
1. node版本过低，nvm切换不生效
> 解决：卸载旧的node.js，nvm 安装node
> nvm install latest
> nvm use 18.8.0
> node -v

2. yarn dev 报错 error: Unexpected end of file
> 解决：删除父目录的jsconfig.json

### 监听器watch
1. watch(()=> person.name, (newValue, oldValue)=>{}, {immediate:true})
> 监听多个数据源，watch触发次数可以使用nextTick async/await
> 监听对象时，数据源是ref、rective、getter会有不同的表现

### vue-router 需要结合实践

> 声明式用法、编程式用法
- <router-link :to="...">
> router.push({name: '', params: ''})
> router.push({path: '', query: ''})
- 配置meta可以用作权限控制，router.beforeEach

```js
  router.push({ path: '/detail', query: { fileId } }) // 地址栏：...?fileId=sr_zys2_hit_2
  router.push({ name: 'Detail', params: { fileId } }) // 需要配置path: '/detail/:fileId' 地址栏：.../detail/sr_zys2_hit_2
```

### 获取元素
```js
<el-row ref="tableRef" justify="center"/>
const tableRef = ref()
tableRef.value.$el
```

### 如何扫码登录？
#### 需要在微信开发平台注册应用(要认证材料)

### 如何启动项目
> npm run dev

### 组件传参方式
1. props
> 子组件定义

### 正则匹配替换
> 多个词替换不同文本，使用replaceAll逐个来写

### ts中vuex的封装demo

### Map和Object的区别
> Map会保持元素的顺序，Object的key是乱的
> Map的key可任意类型

### 跳转页面不刷新
> 仔细阅读文档

### vuex 存储一个对象
> 类型泛型定义好，比如Map<string, string>、Array<string>

### 对vuex的存储对象直接赋值可以吗？store.state.foo = 123
> 对string或array操作可以响应式

### 条件渲染不出来图片
> 


```js
  cos.deleteMultipleObject({
    Bucket: Bucket + '-' + AppId,
    Region,
    Objects: [
      { Key: key }
    ]
  }, function (err, data) {
    console.log('minigood-uploadMedia-err', JSON.stringify(err))
    console.log('minigood-uploadMedia-data', JSON.stringify(data))
  });
```


        

月读·觉醒前_触碰
高桥广树
私(わたし)に何(なに)を望(のぞ)む、さあ、言(い)ってご覧(らん)
想要向我索求些什么呢，我准许了，尽管说说看
watashi ni naniwo nozomu saa itte goran


禅心云外镜_触碰
村濑步
万(ばん)物(ぶつ)には心(こころ)がある、君(きみ)と僕(ぼく)と同(おな)じ様(よう)に
众生有请，情本存于你我心中
ban butsu niwa kokoro ga aru kimito bokuto onaji youni
