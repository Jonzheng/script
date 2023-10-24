// import { decryptToString, encryptToString } from './xxtea'
const xxtea = require('./xxtea.js')

const arr = [{val:12,on: false},{val:11,on: false},{val:10,on: false},{val:9,on: false},{val:8,on: false},{val:7,on: false},{val:6,on: false},{val:5,on: false},{val:4,on: false},{val:3,on: false},{val:2,on: false},{val:1,on: false}]


var endd = xxtea.encryptToString(JSON.stringify(arr), 'mhwii');

console.log('en', endd)

const dedd = xxtea.decryptToString(endd, 'mhwii')

console.log('dedd', dedd)