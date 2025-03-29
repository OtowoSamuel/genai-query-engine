def test_login_success(client):
    response = client.post("/login?username=demo&password=demo123")
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure(client):
    response = client.post("/login?username=wrong&password=wrong")
    assert response.status_code == 401
