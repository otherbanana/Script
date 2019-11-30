#QX转换Surge举例
#QX：^https?:\/\/mp\.weixin\.qq\.com url script-response-body https://raw.com/NobyDa/Wechat.js
#SG:http-response ^https?:\/\/mp\.weixin\.qq\.com requires-body=1,max-size=0,script-path=https://raw.com/NobyDa/Wechat.js
#即前面加了http-response，url script-response-body变成了requires-body=1,max-size=0,script-path=


# 去微博应用内广告 (By yichahucha) 
http-response ^https?://m?api\.weibo\.c(n|om)/2/(statuses/(unread|extend|positives/get|(friends|video)(/|_)timeline)|stories/(video_stream|home_list)|(groups|fangle)/timeline|profile/statuses|comments/build_comments|photo/recommend_list|service/picfeed|searchall|cardlist|page|\!/photos/pic_recommend_status) requires-body=1,max-size=0,script-path= https://raw.githubusercontent.com/yichahucha/surge/master/wb_ad.js
http-response ^https?://(sdk|wb)app\.uve\.weibo\.com(/interface/sdk/sdkad.php|/wbapplua/wbpullad.lua) requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/yichahucha/surge/master/wb_launch.js

# 去微信公众号广告 (By Choler)
http-request ^https://mp\.weixin\.qq\.com/mp/getappmsgad script-path=https://Choler.github.io/Surge/Script/WeChat.js

# 知乎去广告 (By onewayticket255)
http-response ^https://api.zhihu.com/moments\?(action|feed_type) requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/onewayticket255/Surge-Script/master/surge%20zhihu%20feed.js
http-response ^https://api.zhihu.com/topstory/recommend requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/onewayticket255/Surge-Script/master/surge%20zhihu%20recommend.js
http-response ^https://api.zhihu.com/.*/questions requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/JS/Zhihu-ad-answer.js
http-response ^https://api.zhihu.com/market/header requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/onewayticket255/Surge-Script/master/surge%20zhihu%20market.js

# Youtube去广告
http-request ^https://[\s\S]*\.googlevideo\.com/.*&(oad|ctier) script-path=https://Choler.github.io/Surge/Script/YouTube.js

# 流利说•阅读 
http-response ^https?:\/\/vira\.llsapp\.com\/api\/v2\/readings\/(accessible|limitation) requires-body=1,max-size=0,script-path=scripts/llyd.js
