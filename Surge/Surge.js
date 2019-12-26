#QX转换Surge举例
#QX：^https?:\/\/mp\.weixin\.qq\.com url script-response-body https://raw.com/NobyDa/Wechat.js
#SG:http-response ^https?:\/\/mp\.weixin\.qq\.com requires-body=1,max-size=0,script-path=https://raw.com/NobyDa/Wechat.js
#即前面加了http-response，url script-response-body变成了requires-body=1,max-size=0,script-path=



[Script]
# dayone
http-request ^https:\/\/dayone\.me\/api\/users$ script-path=dayone-pre.js
http-response ^https:\/\/dayone\.me\/api\/(users|v2\/users\/account-status)$ requires-body=1,max-size=0,script-path=dayone.js
# 微信去广告
http-request ^https://mp\.weixin\.qq\.com/mp/getappmsgad script-path=https://Choler.github.io/Surge/Script/WeChat.js
# Youtube去广告
http-request ^https://[\s\S]*\.googlevideo\.com/.*&(oad|ctier) script-path=https://Choler.github.io/Surge/Script/YouTube.js
http-request ^https?:\/\/.+\.(my10api|(.*91.*))\.(com|tips|app|xyz)(:\d{2,5})?\/api.php$ script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/JS/91ShortVideo.js
# 流利说•阅读 
http-response ^https?:\/\/vira\.llsapp\.com\/api\/v2\/readings\/(accessible|limitation) requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/otherbanana/Script/master/Files/llyd-s.js,script-update-interval=0
# 91
http-response ^https?:\/\/.+\.(my10api|(.*91.*))\.(com|tips|app|xyz)(:\d{2,5})?\/api.php$ requires-body=1,max-size=0,script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/JS/91ShortVideo.js
# 10010
cron "0 12 * * *" debug=1,script-path=10010+.js
# 京东签到
cron "0 12 * * *" script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/JD-DailyBonus/JD_DailyBonus.js,script-update-interval=0
http-request https:\/\/api\.m\.jd\.com\/client\.action.*functionId=signBeanIndex script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/JD-DailyBonus/JD_GetCookie.js,script-update-interval=0
http-response ^https?://api\.m\.jd\.com/client\.action\?functionId=(wareBusiness|serverConfig) script-path=https://raw.githubusercontent.com/yichahucha/surge/master/jd_price.js,requires-body=1
# 吾爱签到
cron "0 12 * * *" script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/52pojieDailyBonus/52pojie.js,script-update-interval=0
http-request https:\/\/www\.52pojie\.cn\/home\.php\? script-path=https://raw.githubusercontent.com/NobyDa/Script/master/Surge/52pojieDailyBonus/Get-Cookie.js

