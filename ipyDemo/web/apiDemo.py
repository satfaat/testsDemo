import httpx, re, json

URL_JSPLACEHOLDER = "https://jsonplaceholder.typicode.com/"

endpoints = {
    'posts': 'posts'
} 


def get_res(endpoint, auth=None):
    url = URL_JSPLACEHOLDER + endpoint
    res = httpx.get(url=url, verify=False, headers=auth)
    return res


res = get_res(endpoints.get("posts"))

#print(res.json())
assert res.status_code == 200