/*
Quantumult X 脚本:
[rewrite_local]
#Unlocks
^https:\/\/mb3admin\.com\/admin\/service\/registration\/validateDevice url script-response-body 
[mitm]
hostname = mb3admin.com,
*/

let obj= JSON.parse($response.body);
obj= {
  'cacheExpirationDays': 233,
  'message': 'Device Valid',
  'resultCode': 'GOOD'
};

var modifiedStatus = 'HTTP/1.1 200 OK';

$done({body: JSON.stringify(obj)},status: modifiedStatus);
