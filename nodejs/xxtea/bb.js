function encry(code){
    let c = ''
    for(let i=0; i<code.length; i++){
        c += String.fromCharCode(code.charCodeAt(i) + i % 11);
    }
    return c;
}

function decry(code){
    let c = ''
    for(let i=0; i<code.length; i++){
        c += String.fromCharCode(code.charCodeAt(i) - i % 11);
    }
    return c;
} 

const str = JSON.stringify({ titleArr: ["冥灯龙：1234"], treeArr: ["灭尽龙：asddsd"] })

console.log(str)
let en = encry(str)
console.log('en', en)
console.log(decry(en))


function reverStr(code){
    let arr = []
    let sp = code.slice(0, 5)
    for (let idx = 0; idx < code.length; idx += 5) {
        arr.push(code.slice(idx, idx + 5))
    }
    return arr.reverse().join('');
}


// cc = '[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]'

// restr = reverStr(cc)
// console.log('1', restr)
// console.log('2', reverStr(restr))
// console.log('3', ss == decry(encry(ss)))
// console.log('4', JSON.parse(decry(encry(ss))))

const encry2 = function(code) {
    let c = ''
    for(let i=0; i<code.length; i++){
        let cd = code.charCodeAt(i)
        // console.log(cd, String.fromCharCode(cd))
        if (cd > 19968) {
            cd = cd + i % 13
        } else {
            cd = cd + i % 7 - 7
        }
        c += String.fromCharCode(cd);
    }
    return c;
}

function decry2(code){
    let c = ''
    for(let i=0; i<code.length; i++){
        let cd = code.charCodeAt(i)
        if (cd > 19968) {
            cd = cd + i % 13
        } else {
            cd = cd - i % 7 + 7
        }
        c += String.fromCharCode(cd);
    }
    return c;
  }

ds = JSON.stringify([{"weak":"为禁止进入的危险区域该国王城之中。现已成时的王国后，就栖息在之间毁灭了某个繁盛一事中的传说之龙","val": 'whet: "daaazznger:30,warning:60,yellow:20,success:90,dark:200|danger:30,warning:60,yellow:20,success:140,dark:150"'}])

edd = encry2(ds)

console.log(ds)
console.log(edd)
console.log(decry2(edd))
console.log(String.fromCharCode(19968))
console.log(String.fromCharCode(40869))

