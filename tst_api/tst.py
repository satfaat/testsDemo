import requests

server = 'http://bzteltestapi.pythonanywhere.com/'
api_users = server + 'users'


# Create User
# username length = 50
username_50 = {
    "username": "ivanaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "password1": "12345678912345678912",
    "password2": "12345678912345678912"
}
#print(len(username_50['username']))

username_32 = {
    "username": "ivanaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "password1": "12345678912345678912",
    "password2": "12345678912345678912"
}

def create_user(api, json):
    res = requests.post(api, json=json)
    print(f'TEXT: {res.text}')
    print(f'JSON: {res.json}')
    if res.status_code !=201:
        print(res.raise_for_status())
    print(res.text)
    
res = requests.post(api_users, json=username_32)
# print(res.status_code)
# print(res.headers)
# print(res.encoding)
print(f'TEXT: {res.text}')
print(f'JSON: {res.json}')
# print(res.content)
# print(res.url)
if res.status_code !=201:
    print(res.raise_for_status())
print('Created user. ID: {}'.format(res.json()['id']))