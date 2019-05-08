### Wechat Kuakua chatbot
Wechat is a the dominant Chinese social networking platform. This project intends to create a chatbot that replies to people in compliments, which means "kuakua" in Chinese.  

#### itchat: auto reply using tuling api
The [auto-reply]('./auto_reply_tulingAPI') chat bot use [tuling API](http://www.turingapi.com/), 
Apply a chatbot and get a api url like,
```python
apiUrl = 'http://www.tuling123.com/openapi/api'
```
Note down the key when apply and then get thereponse from the API
```python
data = {'key': KEY, 'info': msg, 'userid' :'wechat-robot',}    
try:        
	r = requests.post(apiUrl, data=data).json()        
	return r.get('text')    
except:        
		return 
```
thhen itchat would help reply the response from the API to Wechat.

#### A easier version


#### using nlp library
[https://github.com/xiaopangxia/kuakua_robot]
相似度采用TF-IDF、LSI、LDA等，搜索top4相似话题的回复，从中随机返回表扬语句，效果还不错。 

语料来自豆瓣表扬小组，详见
[https://github.com/xiaopangxia/kuakua_corpus]

#### Run
Tp run the program, cd into the directory and run python3
```
python3 file_name
```
Need to import [`itchat`]('https://github.com/littlecodersh/ItChat'), an easy-to-use personal wechat API that enables wechat to auto-apply messages, [`jieba`]('https://github.com/fxsjy/jieba') a Chinese word segmentation module, and ['']()
Recommend `virtualenv` to develop the program.