import json
import pytest
from api import app 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_clean_string_endpoint_with_null_values(client):
    # Test with a raw string containing NULL values
    data = {'raw_string': '2076,3B,NULL,19C,NULL,138D,NULL'}
    response = client.post('/clean_string', json=data)
    assert response.status_code == 200
    assert json.loads(response.data)['cleaned_string'] == '138D,19C,3B,2076'

def test_clean_string_endpoint_without_null_values(client):
    # Test with a raw string containing no NULL values
    data = {'raw_string': '2076,3B,19C,138D'}
    response = client.post('/clean_string', json=data)
    assert response.status_code == 200
    assert json.loads(response.data)['cleaned_string'] == '138D,19C,3B,2076'