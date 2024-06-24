import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data(client):
    account_id = "123245"
    response = client.get(f'/{account_id}/data')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['accountId'] == account_id
    assert 'timestamp' in json_data
    assert 'data' in json_data


