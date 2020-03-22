if flow.request.url.endswith("itunes.apple.com/WebObjects/MZFinance.woa/wa/inAppRegrantPurchaseHistory"):
    appname = 'com.suwen.DeviceInfo'
if appname in flow.request.get_text():
   flow.response.set_text(real recipt)
