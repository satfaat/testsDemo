from typing import Any, Dict
import httpx
import re
import json
import pydantic
from Endpoints import Endpoints
from config import config


def get_res(endpoint, auth=None) -> httpx.Response:
    url: Any = config.URL_JSPLACEHOLDER + endpoint
    res: httpx.Response = httpx.get(url=url, verify=False, headers=auth)
    return res


def test_get_posts() -> None:
    res: httpx.Response = get_res(Endpoints.POSTS)
    # print(res.json())
    # then:
    assert res.status_code == 200
    assert res.json()[0]['userId'] == 1


class Post(pydantic.BaseModel):
    title: str
    body: str
    userId: int


post1 = Post(
    title="New title",
    body="New body",
    userId=1)
post1_json: Dict[str, Any] = post1.dict()
print(post1_json)

post2: dict[str, Any] = {
    "title": "jsonplaceholder good for practice",
    "body": "Somthing real to get response",
    "userId": 1
}


def create_post(endpoint, dt) -> httpx.Response:
    url: Any = config.URL_JSPLACEHOLDER + endpoint
    res: httpx.Response = httpx.post(url=url, verify=False, json=dt)
    return res


def test_create_post() -> None:
    res: httpx.Response = create_post(Endpoints.POSTS, post1_json)
    assert res.status_code == 201
    print(res.json())
