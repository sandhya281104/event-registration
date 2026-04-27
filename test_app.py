from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_submit():
    client = app.test_client()
    response = client.post('/submit', data={
        'name': 'Test',
        'email': 'test@gmail.com'
    })
    assert response.status_code == 200