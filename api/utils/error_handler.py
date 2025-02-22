"""
Handles error cases and returns the appropriate error codes.
"""

from src.schemas.exception.exception_template import BasicException
from utils.logger import Logger


class ErrorHandler:
    """
    Logs errors and returns the appropriate error codes.
    """
    def __init__(self):
        self.logger = Logger()
    
    def invalid_credentials_error(self):
        """
        Raises an error if incorrect credentials are used to access the API
        """
        self.logger.log_error(f"Invalid credentials.")
        raise BasicException(code=401, detail=f"Invalid credentials.")
