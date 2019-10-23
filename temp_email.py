import requests
import json,time,re
new_email_list = []
id_list = []
code_list = []
def get_new_email(new_email_list):
    url = 'https://linshiyouxiang.net/api/v1/mailbox/keepalive?mailbox='
    response = requests.get(url)
    data = json.loads(response.text)
    new_email = data['mailbox']
    new_email_list.append(new_email)
    email = '%s@linshiyouxiang.net'%new_email
    print(email)
    return email
def get_email_content(new_email_list,id_list):

    houzhui = str(new_email_list[0])
    url = 'https://linshiyouxiang.net/api/v1/mailbox/%s'%houzhui
    print('开始循环拿去后缀Id')
    while True:
        response = requests.get(url)
        html = response.text
        time.sleep(2)
        if len(response.text) != 3:
            break
    data = json.loads(response.text)
    id = data[0]['id']
    id_list.append(id)
    print(id)
    print('已经拿到ID')
    return id
def get_code(id_list,new_email_list,code_list):
    id = str(id_list[0])
    houzhui = str(new_email_list[0])
    url = 'https://linshiyouxiang.net/mailbox/%s/%s'%(houzhui,id)
    print('开始根据id获取code')
    response = requests.get(url)
    html = response.text
    reg = re.compile('<p>您的邮箱验证代码为: <b>(.*?)</b>，请在网页中填写，完成验证')
    code = reg.findall(html)
    code_list.append(code[0])
    print(code[0])
    return code[0]
# get_new_email()
# get_email_content(new_email_list)
# get_code(id_list,new_email_list,code_list)
# code = code_list[0]