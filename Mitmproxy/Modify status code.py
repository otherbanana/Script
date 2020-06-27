##Modify status_code
  if flow.request.url.endswith("www.example.com"):
   flow.request.status_code = 200
   flow.response.status_code = 200
