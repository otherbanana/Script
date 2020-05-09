##Modify headers
  if flow.request.url.endswith("www.example.com"):
   flow.request.headers['ML-Authorization'] = 'A'
   flow.request.headers['ML-DeviceID'] = 'B'
   flow.request.headers['User-Agent'] = 'C'
   flow.response.headers['Cookie'] = 'D'
   flow.response.headers['Accept-Language'] = 'E'
