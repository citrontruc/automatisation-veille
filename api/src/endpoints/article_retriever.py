"""
Endpoint so our user can specify which articles he wants to retrieves.
"""

from fastapi import APIRouter, Request
import json

from src.schemas.input.input_template import ResearchInputSchema
from src.schemas.output.output_template import ResearchOutputSchema
from src.research.research_handler import ResearchHandler
from src.utils.authenticator import Authenticator
from src.utils.logger import Logger


# We define all the routes related to document treatment
router = APIRouter()
authenticator = Authenticator()
logger = Logger()

@router.get("/research", tags=["research"], response_model=ResearchOutputSchema)
async def research(request: Request, query: ResearchInputSchema):
    """
    Endpoint to generate a summary
    input:
        query (dict)
    output
        (dict)
    """
    authenticator.check_api_key(request.headers.get("Authorization"))
    query_dict = query.model_dump()
    logger.log_info(f"Requête envoyée sur le endpoint research avec le contenu suivant : {json.dumps(query_dict)}")
    research_handler = ResearchHandler(query_dict["search_type"], query_dict["llm_type"])
    url_list, content_list = research_handler.search(query_dict["topic"])
    print(url_list)
    clean_content = research_handler.clean_page_content(content_list)
    for i in range(len(url_list)):
        if "reddit" not in url_list[i] and "steamcommunity" not in url_list[i]:
            clean_content[i]["url"] = url_list[i]
    return {"response" : clean_content}
