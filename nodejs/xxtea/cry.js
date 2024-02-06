const crypto = require('crypto');
const hash = crypto.createHash('sha1');

key = hash.update('ofsjapor').digest('hex')

console.log('kry', key)