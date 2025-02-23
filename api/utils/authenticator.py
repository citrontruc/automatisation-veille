"""
An object to check user credentials depending on authentication method
"""

from dotenv import load_dotenv
from fastapi import Security
from fastapi.security import APIKeyHeader
import hashlib
import os

from utils.error_handler import ErrorHandler

load_dotenv()


class Authenticator:
    """
    A parent class that can be used to check user credentials (TODO)
    """
    def __init__(self):
        self.HASHED_API_KEY = os.getenv("HASHED_API_KEY")
        self.error_handler = ErrorHandler()

    def check_api_key(self, api_key: str = Security(APIKeyHeader(name="Authorization", auto_error=True))):
        """
        Check if the input key corresponds to the 
        input:
            api_key (str)
        output:
            None
        """
        if not api_key:
            self.error_handler.invalid_credentials_error()
        if not hashlib.sha256(api_key.encode()).hexdigest() == self.HASHED_API_KEY:
            self.error_handler.invalid_credentials_error()
    
    def check_access_token(self, access_token):
        """
        Uses Azure entra-id to check if the user access token is a valid token
        """
        pass
