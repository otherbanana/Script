from mitmproxy import ctx, http 
import json

class Modify: 
 def response(self, flow): 
  if flow.request.url.startswith("https://api.termius.com/api/v3/bulk/account/"): 
   obj=json.loads(flow.response.get_text()) 
   obj["account"]["pro_mode"] = True 
   obj["account"]["plan_type"]="Premium" 
   obj["account"]["user_type"]="Premium" 
   obj["account"]["current_period"]["until"]="2020-10-10T03:27:34" 
   flow.response.set_text(json.dumps(obj))
   
  if flow.request.url.startswith("https://license.pdfexpert.com/api/1.0/pdfexpert6/subscription/refresh"): 
   obj = {'originalTransactionId':'20000618444996','subscriptionState':'trial','isInGracePeriod':False,'subscriptionExpirationDate':'13:15 03/11/2099','subscriptionAutoRenewStatus':'autoRenewOn','isEligibleForIntroPeriod':False,'isPDFExpert6User':False,'subscriptionReceiptId':'1572178404000'} 
   flow.response.set_text(json.dumps(obj)) 
   
  if flow.request.url.startswith("https://api.calm.com/me"): 
   obj = json.loads(flow.response.get_text()) 
   obj["subscription"] = {'in_free_trial_window':True,'subscription_plan':'com.calm.yearly.trial.one_week.usd_50','began':'2019-04-22T12:12:54.000Z','is_lifetime':True,'valid':True,'is_renewable':True,'is_in_billing_retry_period':False,'will_renew':True,'expires':'2099-04-29T12:12:54.000Z','user_id':'KgagpU1URv','type':'ios','is_canceled':False,'free_trial_began':'2019-04-22T12:12:54.000Z','coupon_used':False,'has_ever_done_free_trial':True,'is_free':False,'ios_details':{'product_id':'com.calm.yearly.trial.one_week.usd_50','began':'2019-04-22T12:12:54.000Z','is_free_trial':True,'id':'540000370675471','is_canceled':False,'is_renewable':True,'free_trial_ended':'2099-04-29T12:12:54.000Z','free_trial_began':'2019-04-22T12:12:54.000Z','will_renew':True,'original_transaction_id':'540000370675471','expires':'2099-04-29T12:12:54.000Z'},'free_trial_ended':'2099-04-29T12:12:54.000Z'} 
   flow.response.set_text(json.dumps(obj)) 
   
  if flow.request.url.startswith("http://limneos.net/buy.php"): 
   flow.response.set_text('1') 
   
  if flow.request.url.startswith("http://iarrays.com/check/check/keyvalidator.php"): 
   flow.response.set_text('T09PT0NPT0wkQ3JhY2tlZEJ5QHB1bGFuZHJlcw==')
   
  if flow.request.url.startswith("https://kuwo.cn"): 
   obj = json.loads(flow.response.get_text()) 
   vip = '/vip/v2/user/vip' 
   time = '/vip/spi/mservice' 
   if vip in flow.request.url: 
    obj[data]["isNewUser"] = "2"; 
    obj['data']["vipLuxuryExpire"] = "1835312949000"; 
    obj['data']["time"] = "1961170340993"; 
    obj['data']["isYearUser"] = "2"; 
    obj['data']["vipmExpire"] = "1835312949000"; 
    obj['data']["vipOverSeasExpire"] = "1835312949000"; 
    obj['data']["vipExpire"] = "1835312949000"; 
    obj['data']["vip3Expire"] = "1835312949000"; 
    flow.response.set_text(json.dumps(obj)) 
   if time in flow.request.url: 
    obj["isVIPMAutoPay"] = 2; 
    obj["isVIPLuxAutoPay"] = 2; 
    flow.response.set_text(json.dumps(obj)) 
    
  if flow.request.url.startswith("https://vsco.co/api/subscriptions/2.1/user-subscriptions"):
   obj = json.loads(flow.response.get_text())
   obj["user_subscription"] = {'user_id':54624336,'subscription_code':'VSCOANNUAL','sku':'VSCOANNUAL','expired': False,'starts_on_sec':1560831070,'expires_on_sec':16555360940000,'last_verified_sec':15608310700000,'canceled_at_sec':None,'source':1,'payment_type':2,'invalid_reason':2,'is_active':True}
   flow.response.set_text(json.dumps(obj))
   
   
  if flow.request.url.startswith("https://biz.caiyunapp.com/v2/user?app_name=weather"):
   obj = json.loads(flow.response.get_text())
   obj['result']['xy_vip_expire'] = "4096483190";
   obj['result']['is_vip'] = True
   obj['result']['vip_expired_at'] = "4096483190";
   obj['result']['is_xy_vip'] = True
   flow.response.set_text(json.dumps(obj))
  
  if flow.request.url.startswith("https://dida365.com/api/v2/user/status"):
   obj = json.loads(flow.response.get_text())
   obj['proEndDate'] ="2099-01-01T00:00:00.000+0000"
   obj['needSubscribe'] = False;
   obj['pro'] = True
   flow.response.set_text(json.dumps(obj))
  
  if flow.request.url.startswith("https://ticktick.com/api/v2/user/status"):
   obj = json.loads(flow.response.get_text())
   obj['proEndDate'] = "2099-01-01T00:00:00.000+0000",
   obj['needSubscribe'] = False;
   obj['pro'] = True
   flow.response.set_text(json.dumps(obj))
   
  if flow.request.url.startswith("https://apimboom2.globaldelight.net/itunesreceipt_v2.php"):
   obj = json.loads(flow.response.get_text())
   obj = {
 "status": "0",
 "receipt-data": {
  "status": 0,
  "environment": "Production",
  "receipt": {
   "receipt_type": "Production",
   "adam_id": 1065511007,
   "app_item_id": 1065511007,
   "bundle_id": "com.globaldelight.iBoom",
   "application_version": "1.4.70002",
   "download_id": 22057166984396,
   "version_external_identifier": 832251566,
   "receipt_creation_date": "2019-10-25 01:51:02 Etc/GMT",
   "receipt_creation_date_ms": "1571968262000",
   "receipt_creation_date_pst": "2019-10-24 18:51:02 America/Los_Angeles",
   "request_date": "2019-10-25 01:53:35 Etc/GMT",
   "request_date_ms": "1571968415590",
   "request_date_pst": "2019-10-24 18:53:35 America/Los_Angeles",
   "original_purchase_date": "2019-10-25 01:43:54 Etc/GMT",
   "original_purchase_date_ms": "1571967834000",
   "original_purchase_date_pst": "2019-10-24 18:43:54 America/Los_Angeles",
   "original_application_version": "1.4.70002",
   "in_app": [
    {
     "quantity": "1",
     "product_id": "com.globaldelight.iBoom.7DayFree1YearIntroPack",
     "transaction_id": "20000617694038",
     "original_transaction_id": "20000617694038",
     "purchase_date": "2019-10-25 01:50:51 Etc/GMT",
     "purchase_date_ms": "1571968251000",
     "purchase_date_pst": "2019-10-24 18:50:51 America/Los_Angeles",
     "original_purchase_date": "2019-10-25 01:50:51 Etc/GMT",
     "original_purchase_date_ms": "1571968251000",
     "original_purchase_date_pst": "2019-10-24 18:50:51 America/Los_Angeles",
     "expires_date": "2029-11-01 01:50:51 Etc/GMT",
     "expires_date_ms": "1888167051000",
     "expires_date_pst": "2029-10-31 18:50:51 America/Los_Angeles",
     "web_order_line_item_id": "20000194718574",
     "is_trial_period": "true",
     "is_in_intro_offer_period": "false"
    }
   ]
  },
  "latest_receipt_info": [
   {
    "quantity": "1",
    "product_id": "com.globaldelight.iBoom.7DayFree1YearIntroPack",
    "transaction_id": "20000617694038",
    "original_transaction_id": "20000617694038",
    "purchase_date": "2019-10-25 01:50:51 Etc/GMT",
    "purchase_date_ms": "1571968251000",
    "purchase_date_pst": "2019-10-24 18:50:51 America/Los_Angeles",
    "original_purchase_date": "2019-10-25 01:50:51 Etc/GMT",
    "original_purchase_date_ms": "1571968251000",
    "original_purchase_date_pst": "2019-10-24 18:50:51 America/Los_Angeles",
    "expires_date": "2029-11-01 01:50:51 Etc/GMT",
    "expires_date_ms": "1888167051000",
    "expires_date_pst": "2029-10-31 18:50:51 America/Los_Angeles",
    "web_order_line_item_id": "20000194718574",
    "is_trial_period": "true",
    "is_in_intro_offer_period": "false",
    "subscription_group_identifier": "20461753"
   }
  ],
  "pending_renewal_info": [
   {
    "auto_renew_product_id": "com.globaldelight.iBoom.7DayFree1YearIntroPack",
    "original_transaction_id": "20000617694038",
    "product_id": "com.globaldelight.iBoom.7DayFree1YearIntroPack",
    "auto_renew_status": "1"
   }
  ]
 },
 }
   flow.response.set_text(json.dumps(obj))
  
  if flow.request.url.startswith("https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/prod-4-syncPurchases/invocations"):
   obj = json.loads(flow.response.get_text())
   obj = {
  "purchases": [
    {
      "topUpId": "iapPremiumYearly70FreeTrial",
      "provider": "apple",
      "receipt": "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",
      "status": "valid",
      "purchaseDate": 1555871338000,
      "expirationDate": 4080738538000,
      "transactionId": "540000370461013"
    }
  ]
}
   flow.response.set_text(json.dumps(obj))
   
  if flow.request.url.startswith("https://api.interpreter.caiyunai.com/v1/user/"):
   obj = json.loads(flow.response.get_text())
   obj['user']['mvp_count']="99999"
   obj['user']['point']="99999"
   obj['user']['biz']['is_xy_vip'] = True;
   obj['user']['biz']['xy_vip_expire'] = "4096483190";
   flow.response.set_text(json.dumps(obj))
   
  if flow.request.url.startswith("https://book.haitunwallet.com/app/vip/status"):
   obj = json.loads(flow.response.get_text())
   obj = {
          "data": {
                   "level": 2,
                   "status": 1,
                   "openTime": "2099-10-20",
                   "startTime": "2099-10-20",
                   "endTime": "2099-10-20",
                   "shareToken": ""
                                   },
                   "code": 0,
                   "msg": "返回成功"
                                   };
   flow.response.set_text(json.dumps(obj))


  if flow.request.url.startswith("https://mubu.com/api/app/user/info"):
   obj = json.loads(flow.response.get_text())
   obj = {
   "code": 0,
   "data": {
      "encryptPassword": None,
      "id": 4962624,
      "level": 1,
      "name": "Lucien",
      "passSecure": False,
      "phone": None,
      "photo": "https://mubu.com/photo/fa3b0a2d-039b-433a-aad8-b87d9e558df6.jpg",
      "qqId": None,
      "qqName": None,
      "vipEndDate": "20330101",
      "wxId": "oahEws_u3tYBYU6V-d3zM17pQdek",
      "wxName": "Lucien"
   },
   "msg" : None
};
   flow.response.set_text(json.dumps(obj))
   
  if flow.request.url.startswith("https://backend.getdrafts.com/api/v1/verification"):
   obj = json.loads(flow.response.get_text())
   obj = {
  "active_expires_at": "2037-01-01T00:00:00Z",
  "is_subscription_active": True,
  "active_subscription_type": "premium",
  "is_blocked": False
};
   flow.response.set_text(json.dumps(obj))

  if flow.request.url.startswith('https://api.gotokeep.com'):  
                #print(flow.request.url)  仅surge可以用            
                vip1 = 'dynamic'
                vip2 = 'subject'
                if vip1 in flow.request.url:
                    obj = json.loads(flow.response.get_text())
                    #print(obj)
                    obj['data']['permission']['isMembership'] = True
                    obj['data']['permission']['membership'] = True
                    obj['data']['permission']['inSuit'] = True
                    flow.response.set_text(json.dumps(obj))
                if vip2 in flow.request.url:
                    obj = json.loads(flow.response.get_text())
                    #print(flow.request.url)
                    for i in range(len(obj['data']['subjectInfos'])) :
                        obj['data']['subjectInfos'][i]['needPay'] = False                          
                        #print('keep')  
                    #print(obj['data']['subjectInfos'])            
                    flow.response.set_text(json.dumps(obj))

  if flow.request.url.startswith("https://p.du.163.com/gain/readtime/info.json"):
   obj = json.loads(flow.response.get_text())
   obj['tradeEndTime'] = 1679685290000
   flow.response.set_text(json.dumps(obj))

  if flow.request.url.startswith("https://cn.eagle.cool/register"):
    obj = json.loads(flow.response.get_text())
    obj = {
 "success": True,
 "message": "註冊成功",
 "license": {
  "devices": "[{\"activeAt\":1575269201873,\"name\":\"localhost\",\"platform\":\"Darwin\",\"machineID\":\"6812852037901449dbec9341d023b547294f4e3dbd0d922fb690a5e008220ba4\"}]",
  "email": "472085476@qq.com",
  "_id": "5de4b1d8e6561d7e12460f8b",
  "updatedBy": "5ab0ee5917f78e134b18a373",
  "updatedAt": "2020-12-02T06:46:41.890Z",
  "createdBy": "5ab0ee5917f78e134b18a373",
  "createdAt": "2020-12-02T06:40:24.205Z",
  "createdDate": "2020-12-01T18:40:23.000Z",
  "code": "TRIAL-DA82-48D8-8727-9B0F",
  "__v": 0,
  "deviceCount": 3
 },
 "verificatioCode": "M5J0JES8+2/8gCstj8l9Cux4J6TOgJLoVrWfr64n4778+Uc4OAHGVPUV+INVNCV5mOKj5z9bV+pyOerGULTzI7DcBpqH60waL5v/M2M3sZ5qyW8j/O8MkHcaJ5c4taAuz2jo6IAson+9nGMJT+l9ZtGuLRSwlHzTXzPyMl8gI70vSRjFfafItVaD5dJxGl6e19hzmLvyh3O3HZEmaxMEashLza+J70+JbeFhXiXdv9FPERT40UStgGuJSnkPg1Ero6ivbW6yvW1UfjrKjeee9GzGaTxJmNKXFH7wbgtie6JCQwdvU5Qg6YSeSr+Lvwl27b2o/PIDEMvGeE/lrUsIYg=="
}
    flow.response.set_text(json.dumps(obj))
    
  if flow.request.url.startswith("http://m.ktlshu.vip/8/find"):
    flow.response.set_text('vSzghuHsv6yt1HoXJuCZxnPEM6HlqT+buKWPPv4/Yv266mPEJo5helHPELLFjICLITyFqE9jW6mGCxI0SlhHJ4b5NjbR8vXYthcJwKHhLMEe1XPyus8b77RY0i8bl6rfE9qtLTXJYnc5kj6gXmg7/2v5BffUXYO1TinFjKCt2MybymvIoo6/TpqOFjfbqXAqQrwODdktPy/gDVylBr9aGenWwIeLUoxNZvEm8ATUMXinymA4vemCtwZ+9a2LpFKszwrxyKA+5mevEt670b6LPrSsZxnFh1Z5ljB+r3A06yQmHUk1/IW/a7T28++RBlnhu8cyIrNXcoCgyTGDaTr0KsYP1ngdlY12Vz2pBm0I5hyHPK5VytoISNwl8bg8COKVVBxT+aYyoVsRKQLapn30XWeA1xoMelKMs3VE1emiowV1de6vdt11ogrr55UOYdhqg8Pu7wEwtg1at57D+xBB3av+Jf6ZD5L3fh/oBpNy6HF/Ry9nyCpPTGmcB6V5lBQl05cVgQSVC0vCeVHyW3R16sV4BOUgPXUkOlpenVAZ+nY6KAZBLw0MrMJvXMXi7TBw1REH/liACUnDSj67rXOFrVcXqail8gkBQJMidIpJMHw=')
    
    flow.response.set_text(json.dumps(obj))
  
  

 def request(self, flow): 
  ctx.log.info("modify request form") 
     
addons=[ 
Modify() 
]
