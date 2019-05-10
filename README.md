# Wechat Kuakua chatbot
Wechat is the dominant social networking platform in China. This project is inspired by the trend that people gives compliments to each other in wechat group, which means "kuakua" in Chinese.  

### itchat: auto reply chatbot using tuling api
The [auto-reply](/auto_reply_tulingAPI) chat bot use [tuling API](http://www.turingapi.com/), 
Apply a tuling chatbot and get a API url from the website, such as
```python
apiUrl = 'http://www.tuling123.com/openapi/api'
```
Note down the key when apply and then get the auto-response from the API
```python
data = {'key': KEY, 'info': msg, 'userid' :'wechat-robot',}    
try:        
	r = requests.post(apiUrl, data=data).json()        
	return r.get('text')    
except:        
	return 
```
Then itchat would help reply the response back from the API to Wechat using the following line before the function header.
```python
@itchat.msg_register(itchat.content.TEXT)
```
Use followig code to run itchat.
```python
itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
```

### Wechat_kuakua1.0

**Reference**: [A Wechat Article](https://mp.weixin.qq.com/s/EssVIqNXLDWn_HubHzJ8Mw)

`wechat_kuakua1.0` uses a dict of corresponding keywords with an array of prepared replies. The program then matches words appearing in the message sent by the user with the keywords and replies randomly in the corresponding array of prepared replies. 
)
```python
REOLY = {'keyword': ['sentence 1', 
                    'sentence 2'],
        'keyword2': ['sentence 3',
                    'sentence 4']}
```
```python
@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
    group_name = 'group name' # put wechat group name here
	match = re.search('keyword', msg['Text'])
    if match:
        randomIdx = random.randint(0, len(REPLY['keyword']) - 1)
        itchat.send('@' + '%s\n%s' % (username, REPLY['keyword'][randomIdx]), msg['FromUserName'])
```
Note: set a wechat group, and set its name variable `group_name` and all the conversation would only take place in that wechat_group.

### Using Chinese Nlp Library
**[Reference](https://github.com/xiaopangxia/kuakua_robot)**

The [corpus](https://github.com/xiaopangxia/kuakua_corpus) is crawled from douban. We parse the sentences of messages and train the model use `Genism`.

First load the question and answer from the corpus into an array of messages, and an corresponding array of lists of replies. The index is used to connect the message and its replies.

Then we parse the received message and compared it to the sentences of messages we have in the corpus. The similarity matrix can be expressed by models *TF-IDF*, *LSI*, *LDA* etc. We search for the top 4 similar sentence and choose a random one, reply by its list of replies in the corpus.


### Run
Tp run the program, cd into the directory and run python3, such as
```
python3 wechat_kuakua2.0.py
python3 wechat_kuakua1.0.py
```
Need to install and import 
- **[itchat](https://github.com/littlecodersh/ItChat)**, an easy-to-use personal wechat API that enables wechat to auto-apply messages, 
- **[jieba](https://github.com/fxsjy/jieba)**, a Chinese word segmentation module, and 
- **[Genism](https://pypi.org/project/gensim/)**, a Python library for topic modelling, document indexing and similarity retrieval with large corpora.
Recommend `virtualenv` to develop the program.

A useful [article](https://www.jianshu.com/p/a1fc25cd9c4b) to understand how genism works.