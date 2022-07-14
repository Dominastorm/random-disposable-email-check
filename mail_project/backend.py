import random
import string
import requests

API = 'https://www.1secmail.com/api/v1/'

def generate_email():
    domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
    domain = random.choice(domainList)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
    email = username + '@' + domain

    req = requests.get(f"{API}?login={username}&domain={domain}")
    
    if req.status_code == 200:
        return email
