"""
Calls an API to retrieve information
"""

from dotenv import load_dotenv
import os
import requests

load_dotenv()


class APIClient():
    """
    Calls an API to retrieve information
    """
    def __init__(self):
        self.API_URL = os.getenv("API_URL")
        self.API_KEY = os.getenv("API_KEY")

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
        answer = requests.get(f"{self.API_URL}/{endpoint}", headers=headers, json=content)
        return answer