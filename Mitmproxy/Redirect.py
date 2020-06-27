##Redirect
##https://example.com/receipt redirect to https://raw.githubusercontent.com/otherbanana/Scripting/master/Adguard.rsp
  if flow.request.url.startswith("https://example.com/receipt"):
   flow.request.host = 'raw.githubusercontent.com'
   flow.request.path = '/otherbanana/Scripting/master/Adguard.rsp'
   obj = json.loads(flow.response.get_text())
   obj = {"products":[{"product_id":"com.adguard.lifetimePurchase","premium_status":"ACTIVE"}]}
   flow.response.set_text(json.dumps(obj))
