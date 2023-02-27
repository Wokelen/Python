from app import app
from pytest import fixture
from utils import *

@fixture()
def posts_keys():
    return {"poster_name","poster_avatar","pic",
    "content","views_count","likes_count","pk"}

@fixture()
def client():
    return app.test_client()


def test_posts(client):
    response = client.get("/api/")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_post(client, posts_keys):
    response = client.get("/api/post/1")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json.keys() == posts_keys

def test_load_posts():
    response = load_posts()
    assert isinstance(response, list)

def test_load_post(posts_keys):
    response = load_post(1)
    assert isinstance(response, dict)
    assert response.keys() == posts_keys

def test_load_comments():
    response = load_comments(1)
    assert isinstance(response, list)
    