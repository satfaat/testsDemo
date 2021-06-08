import requests
import json
 

username_50 = {
    "username": "ivanaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "password1": "12345678912345678912",
    "password2": "12345678912345678912"
}

username_32 = {
    "username": "ivanaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "password1": "12345678912345678912",
    "password2": "12345678912345678912"
}

login_32 = {
    "username": username_32["username"],
    "password": username_32["password1"]
}

#memo_status_ids = ['TODO', 'INPROGRESS', 'DONE', 'CANCELED']
memo_todo = {
    'text': 'Some text',
    'status': 'TODO'
}

memo_inprogress = {
    'text': 'Some text',
    'status': 'INPROGRESS'
}

memo_done = {
    'text': 'Some text',
    'status': 'DONE'
}

memo_canceled = {
    'text': 'Some text',
    'status': 'CANCELED'
}

server = 'http://bzteltestapi.pythonanywhere.com/'
apis = {
    'users': server + 'users',
    'todos': server + f"todos/{username_32.get('username')}/{1}",
    'login': server + 'login'
}

def create_user(url_api, json):
    res = requests.post(url_api, json=json)
    print(f'TEXT: {res.text}')
    print(f'JSON: {res.json}')
    if res.status_code !=201:
        print(res.raise_for_status())
    print(res.text)

def update_password(url_api, json):
    res = requests.put(url_api, json=json)
    print(f'TEXT: {res.text}')
    print(f'JSON: {res.json}')
    if res.status_code !=201:
        print(res.raise_for_status())
    print(res.text)

def get_token(url_api, json):
    res = requests.post(url_api, json=json)
    if res.status_code !=200:
        print(res.raise_for_status())
    return res.text

token = json.loads(get_token(url_api=apis['login'], json=login_32))
def create_memo(url_api, json, token):
    res = requests.post(
        url_api, 
        json=json, 
        headers={'Authorization': f'Bearer {token.get("access_token")}'}
    )
    print(f'TEXT: {res.text}')
    print(f'JSON: {res.json}')
    print(res.status_code)
    print(f'AUTH: {res.headers}')
    print(res.url)
    if res.status_code !=200:
        print(res.raise_for_status())
    print(res.text)

# create_user(api=apis['users'], json=username_50)
# create_user(api=apis['users'], json=username_32)

create_memo(url_api=apis['todos'], json=memo_todo, token=token)
