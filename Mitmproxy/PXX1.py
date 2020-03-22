if flow.request.url.endswith("itunes.apple.com/WebObjects/MZFinance.woa/wa/inAppRegrantPurchaseHistory")\
and 'com.h3d2.1998cam' in flow.request.get_text():
    flow.response.set_text(real recipt)
