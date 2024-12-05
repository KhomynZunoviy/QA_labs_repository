#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.api_client import APIClient
import pytest
@pytest.fixture(scope="session")
def api_client():
    return APIClient('https://www.saucedemo.com/')

def test_get_endpoint(api_client):
    response = api_client.get('')
    assert response.status_code == 200

