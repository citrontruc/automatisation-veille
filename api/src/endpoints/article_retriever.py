"""
Endpoint so our user can specify which articles he wants to retrieves.
"""

from fastapi import APIRouter, Request
import json

from src.schemas.input.input_template import BasicInputSchema
from utils.authenticator import Authenticator
from utils.logger import Logger


# We define all the routes related to document treatment
router = APIRouter()
authenticator = Authenticator()
logger = Logger()
