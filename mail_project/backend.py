import random
import string
import requests
import time

API = 'https://www.1secmail.com/api/v1/'

def generate_email():
    domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
    domain = random.choice(domainList)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
    email = username + '@' + domain

    req = requests.get(f"{API}?login={username}&domain={domain}")
    
    if req.status_code == 200:
        return email

def check_mailbox(username, domain):
    reqLink = f'{API}?action=getMessages&login={username}&domain={domain}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length > 0:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={username}&domain={domain}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v
           
            return {'Sender': sender, 'Subject': subject, 'Date': date, 'Content': content}
           
def get_inbox(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    while True:
        result = check_mailbox(username, domain)
        if result == None:
            time.sleep(5)
        else:
            return result