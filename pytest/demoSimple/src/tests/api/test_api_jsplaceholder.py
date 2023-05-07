from typing import Any, Dict
import httpx
import re
import json
import pytest
from pytestDemoSimple.src.tests.Endpoints import Endpoints
from pytestDemoSimple.configs.config import config
from pytestDemoSimple.src.tests.api.DTO.PostRecord import Post


@pytest.fixture
def post1():
    post1 = Post(
        title="New title",
        body="New body",
        userId=1)
    return post1.dict()


@pytest.fixture
def post2():
    post2: dict[str, Any] = {
        "title": "jsonplaceholder good for practice",
        "body": "Somthing real to get response",
        "userId": 1
    }
    return post2


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


def create_post(endpoint, dt) -> httpx.Response:
    url: Any = config.URL_JSPLACEHOLDER + endpoint
    res: httpx.Response = httpx.post(url=url, verify=False, json=dt)
    return res


def test_create_post(post1) -> None:
    res: httpx.Response = create_post(Endpoints.POSTS, post1)
    assert res.status_code == 201
    print(res.json())

# @pytest.mark.parametrize('posts', [post1, post2])
# def test_create_post(posts) -> None:
#     res: httpx.Response = create_post(Endpoints.POSTS, posts)
#     assert res.status_code == 201
