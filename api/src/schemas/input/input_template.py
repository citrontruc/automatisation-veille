"""
A class to define what a valid message is.
"""
from pydantic import BaseModel


class BasicInputSchema(BaseModel):
    """
    Class to define a correct input schema
    """
    query: str
