from mitmproxy import ctx, http
import json
import re

class RemoveHeaders:
	def response(self, flow):


####### Test Remo #######
		if flow.request.url.startswith("https://api.faceapp.io/api/v3.3/auth/user/credentials")\
		and ('x-faceapp-errorcode') in flow.response.headers:
			ctx.log.warn("Match Header= [{}]".format(flow.response.headers["x-faceapp-errorcode"]))
			del flow.response.headers['x-faceapp-errorcode']

####### Test Remo-Simple #######
		if flow.request.url.startswith("https://api.faceapp.io/api/v3.3/auth/user/credentials"):
			del flow.response.headers['x-faceapp-errorcode']

addons=[RemoveHeaders()]
