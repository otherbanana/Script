##Modify headers
  if flow.request.url.endswith("www.example.com"):
   flow.request.headers['ML-Authorization'] = 'A'
   flow.request.headers['ML-DeviceID'] = 'B'
   flow.request.headers['User-Agent'] = 'C'
   flow.request.headers['Cookie'] = 'D'
   flow.request.headers['Accept-Language'] = 'E'