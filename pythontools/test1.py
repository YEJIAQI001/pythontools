from functools import reduce
import pandas as pd
import re
import os
import logging
from logging import Logger

logging.basicConfig(level=logging.INFO, format='%(asctime) - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
# %%
with open('E:\\testdoc\\README.txt', 'r', encoding='utf-8') as f:
    # for line in f.readlines():
    #     print(line.strip())  # 把末尾的'\n'删掉
    while True:

        s = f.readline()

        if s == '':
            break

        print(s.strip())
# %%

print(os.name)
print(os.environ.get('PATH'))
# %%
print(os.path.abspath('.'))
# %%
from datetime import datetime

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M:%S')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# %%
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
d['Michael']
# %%
s = set([1, 2, 3, 1])
print(s)
# %%
d = dict(name='Bob', age=20, score=88)
print(d)
# %%
import pickle

pickle.dumps(d)
# %%
# 序列化
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# %%
f = open('dump.txt', 'rb')
e = pickle.load(f)
f.close()
print(e)
# %%
import json

json.dumps(d)
# %%
import time, threading


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
# %%
from urllib import request

with request.urlopen('http://www.douban.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
# %%
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# %%
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# %%
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

#%%
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
#%%
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
#%%
