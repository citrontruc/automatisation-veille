"""
Endpoint so our user can specify which articles he wants to retrieves.
"""

from fastapi import APIRouter, Request
import json

from schemas.input.input_template import ResearchInputSchema
from schemas.output.output_template import ResearchOutputSchema
from research.research_handler import ResearchHandler
from utils.authenticator import Authenticator
from utils.logger import Logger


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
    # Check credentials
    authenticator.check_api_key(request.headers.get("Authorization"))
    
    # Research online information for the given user query
    query_dict = query.model_dump()
    logger.log_info(f"Request received on endpoint research with the following content : {json.dumps(query_dict)}")
    research_handler = ResearchHandler(query_dict["search_type"], query_dict["llm_type"])
    url_list, content_list = research_handler.search(query_dict["topic"])
    
    # Clean content of answers
    clean_content = research_handler.clean_page_content(content_list, query_dict["topic"])
    answer_dict = []
    for i in range(len(url_list)):
        answer_dict.append({"extracted_page" : clean_content[i]})
        answer_dict[-1]["url"] = url_list[i]
    
    # Return response
    return {"response" : answer_dict}
