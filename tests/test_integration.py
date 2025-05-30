from app import app

def test_soma_endpoint():
    client = app.test_client()
    response = client.get('/api/soma/4/5')
    assert response.json['resultado'] == 9