"""
Tests to verify that we can call the defined APIs
"""

from dotenv import load_dotenv
import pytest
import requests
import os


@pytest.mark.parametrize("endpoint, api_key", [(os.getenv("API_BASE_URL"), os.getenv("API_KEY"))])
def test_call_api(endpoint, api_key):
    """
    Test to check if the APIs we need to call are reachable.
    input:
        endpoint (str)
        api_key (str)
    """
    answer = requests.get(endpoint, headers={"Authorization" : api_key})
    assert answer.status_code == 200
