"""
Endpoint so our user can ask to summarize information from multiple sources
"""

from fastapi import APIRouter, Request
import json

from schemas.input.input_template import SummarizationInputSchema
from utils.authenticator import Authenticator
from utils.logger import Logger


# We define all the routes related to document treatment
router = APIRouter()
authenticator = Authenticator()
logger = Logger()
