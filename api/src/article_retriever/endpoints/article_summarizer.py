"""
Endpoint so our user can ask to summarize information from multiple sources
"""

from fastapi import APIRouter, Request
import json

from src.article_retriever.schemas.input.input_template import SummarizationInputSchema
from src.article_retriever.utils.authenticator import Authenticator
from src.article_retriever.utils.logger import Logger


# We define all the routes related to document treatment
router = APIRouter()
authenticator = Authenticator()
logger = Logger()
