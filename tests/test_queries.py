def test_query_endpoint(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/query",
        json={"query": "sales last week"},
        headers=headers
    )
    assert response.status_code == 200
    assert "pseudo_sql" in response.json()["data"]

def test_unauthenticated_query(client):
    response = client.post("/query", json={"query": "test"})
    assert response.status_code == 401

def test_explain_endpoint(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/explain",
        json={"query": "sales by region"},
        headers=headers
    )
    assert response.status_code == 200
    assert "converted to" in response.json()["explanation"]


def test_empty_query(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/query", json={"query": ""}, headers=headers)
    assert response.status_code == 400

def test_sql_injection_attempt(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post(
        "/query",
        json={"query": "'; DROP TABLE sales;--"},
        headers=headers
    )
    # Should fail gracefully, not execute SQL
    assert response.status_code == 400