"""
Calls an API to retrieve information
"""

import requests


class APIClient():
    """
    Calls an API to retrieve information
    """
    def __init__(self, API_BASE_URL, API_KEY):
        self.API_BASE_URL = API_BASE_URL
        self.API_KEY = API_KEY

    def call_api(self, headers, content, endpoint=""):
        """
        Method to call the default API.
        input:
            headers (dict)
            content (dict)
            endpoint (str)
        output:
            (dict)
        """
        answer = requests.get(f"{self.API_BASE_URL}/{endpoint}", headers=headers | {"Authorization" : self.API_KEY}, json=content)
        return answer
