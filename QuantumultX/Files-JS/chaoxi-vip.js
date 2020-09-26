let obj=JSON.parse($response.body)

obj["vip"]["expired_at"] = 1903393240
obj["vip"]["created_at"] = 1590549571
obj["vip"]["is_lifetime_member"] = true
obj["vip"]["is_valid"] = true
obj["premium_type"] = 3
obj["is_paying_premium_user"] = true
body = JSON.stringify(obj);

$done({body:JSON.stringify(obj)})
