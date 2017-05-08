#-*- encoding: utf-8 -*-
import requests
import json
class Confighttp:
	#get
	def get(self,url):
		self=requests.get(url)
		print ('Response:',self.text)
		return self.text	
	#post
	def post(self,url,payload,headers):
		global null
		null=''
		self.url=url
		self.payload=payload
		self.headres=headers
		#self=requests.post(url,data=json.dumps(payload), headers=headers)
		self=requests.post(url,data=payload, headers=headers)
# 		print ("Response:",self.text)
		return self.text
	
