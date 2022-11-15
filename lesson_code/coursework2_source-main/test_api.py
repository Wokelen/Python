from main import app

def test_posts():
    response = app.test_client().get("/api/post/")
    assert isinstance(response.data, list)
    assert response.status_code == 200

def test_post():
    response = app.test_client().get("/api/post/1")
    assert isinstance(response.data, dict)
    assert response.status_code == 200

