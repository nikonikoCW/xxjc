import requests
import re
import base64
import pyperclip
import json
import os
import time
headers = {
    'authority': 'xxjc.pw',
    'method': 'POST',
    'path': '/auth/login',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '26',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':'__cfduid=dde825a385c429177c3b1f8180b9b98991571385339; _ga=GA1.2.1309111820.1571385368; _gid=GA1.2.2080567624.1571385368; ip=389166fd75eb4d2273f7cc78e02444a6; expire_in=1571471852',
    'origin': 'https://xxjc.pw',
    'referer': 'https://xxjc.pw/auth/login',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
def regist_email_code(my_email):
    headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    url = 'https://xxjc.pw/auth/send'
    data={
        'email':my_email
    }
    response = requests.post(url,headers=headers2,data=data,proxies=proxies)
    html = response.text
    data = json.loads(html)
    print(data['msg'])
def regist(my_email,email_code):
    url = 'https://xxjc.pw/auth/register'
    headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    data = {
        'email': my_email,
        'name': 'niconicoxixi',
        'passwd': my_email,
        'repasswd': my_email,
        'wechat': my_email,
        'imtype': '4',
        'code': 0,
        'emailcode':email_code
    }
    response = requests.post(url,headers=headers2,data=data,proxies=proxies)
    response.encoding = 'utf-8'
    html = response.text
    data = json.loads(html)
    print(data['msg'])
def load():
    url = 'https://xxjc.pw/auth/login'
    headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    data = {
        'email': my_email,
        'passwd': my_email,
        'code':''
    }
    response = requests.post(url,headers=headers2,data=data)
    html = response.text
    data = json.loads(html)
    print(data['msg'])
    print('开始构建cookie')
    cookie_data = response.headers['Set-Cookie']
    reg_uid = re.compile('uid=(.*?);')
    reg_email = re.compile('email=(.*?);')
    reg_key = re.compile('key=(.*?);')
    reg_ip = re.compile('ip=(.*?);')
    reg_expire_in = re.compile('expire_in=(.*?);')
    uid = reg_uid.findall(cookie_data)
    email = reg_email.findall(cookie_data)
    key = reg_key.findall(cookie_data)
    ip = reg_ip.findall(cookie_data)
    expire_in = reg_expire_in.findall(cookie_data)
    cookie = '__cfduid=dde825a385c429177c3b1f8180b9b98991571385339; _ga=GA1.2.1309111820.1571385368; _gid=GA1.2.390497948.1571618975; _gat=1; uid=%s; email=%s; key=%s; ip=%s; expire_in=%s;'%(uid[1], email[0], key[0], ip[0], expire_in[0])
    cookie_list.append(cookie)
    print('cookie构建完毕并且添加到集合，准备获取订阅')
def save_account_url(my_email,dingyue):
    with open('jichang.txt' ,'a',encoding='utf-8-sig') as f:
        f.write('账号：'+my_email)
        f.write('                 ')
        f.write('平台：'+'https://xxjc.pw')
        f.write('                 ')
        f.write('时间：' + str(time.strftime("%Y-%m-%d %H:%I:%S", time.localtime( time.time() ) )))
        f.write('                 ')
        f.write('订阅：' + str(dingyue[0]))
        f.write('\n')
        f.close()
def get_link(cookie_list):
    cookie = str(cookie_list[0])
    #print(cookie)
    url = 'https://xxjc.pw/user'
    #cookie2 = '__cfduid=dde825a385c429177c3b1f8180b9b98991571385339; _ga=GA1.2.1309111820.1571385368; _gid=GA1.2.390497948.1571618975; _gat=1; uid=64334; email=ax41etiw%40ncdidi.tk; key=45bcd6aa78d46ba71b270262e9f7c076b4c8ee57ffe0c; ip=aca56569df9d0dfa32e6874742b008c5; expire_in=1571816142;'
    headers2 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'cookie': cookie
    }
    print('开始获取订阅的html，已经构建完头部')
    response =  requests.get(url,headers=headers2)
    html = response.text
    reg = re.compile('<button class="copy-text btn btn-subscription col-xx-12 col-sm-3 col-lg-2" type="button" data-clipboard-text="(.*?)">点击复制</button><br>')
    data = reg.findall(html)
    print(data[0])
    dingyue.append(data[0])


import temp_email
new_email_list = []
id_list = []
code_list = []
#拿到新的邮箱
myemail = temp_email.get_new_email(new_email_list)
my_email = myemail
dingyue = []
cookie_list= []
#发起注册
regist_email_code(my_email)
#去拿验证码
temp_email.get_email_content(new_email_list,id_list)

new_code= temp_email.get_code(id_list,new_email_list,code_list)
email_code = new_code
regist(my_email,email_code)
load()
get_link(cookie_list)
save_account_url(my_email,dingyue)
