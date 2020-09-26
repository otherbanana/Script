var body = $response.body;
var obj = JSON.parse(body);

obj["vip"]["expired_at"] = 1903393240
obj["vip"]["created_at"] = 1590549571
obj["vip"]["is_lifetime_member"] = True
obj["vip"]["is_valid"] = True
obj["premium_type"] = 3
obj["is_paying_premium_user"] = True
body = JSON.stringify(obj);

$done(body);
