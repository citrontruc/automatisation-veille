"""
A script to define our exceptions and how they behave.
"""

class BasicException(Exception):
    """
    A simple class to define our exception types for our error handler.
    """
    def __init__(self, detail: str, code: int):
        self.detail = detail
        self.code = code
