#Redirect
##https://example1.com/receip1t redirect to https://example2.com/receipt2
  if flow.request.url.startswith("https://example1.com/receipt1"):
   flow.request.host = 'example2.com'
   flow.request.path = '/receipt2'
