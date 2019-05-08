#coding=utf8
import requests
import itchat

KEY = '83bf898ff4714b89a47ca7e3b6b51acb' 
def get_response(msg):    
	apiUrl = 'http://www.tuling123.com/openapi/api'    
	data = {'key': KEY, 'info': msg, 'userid' :'wechat-robot',}    
	try:        
		r = requests.post(apiUrl, data=data).json()        
		return r.get('text')    
	except:        
		return 

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):    
	defaultReply = 'I received: ' + msg['Text']    
	reply = get_response(msg['Text'])    
	return reply or defaultReply 

itchat.auto_login(hotReload=False)
itchat.run()