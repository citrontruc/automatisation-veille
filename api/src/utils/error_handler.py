"""
Handles error cases and returns the appropriate error codes.
"""

from src.schemas.exception.exception_template import BasicException
from src.utils.logger import Logger


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
    
    def model_not_supported_error(self, model_name=""):
        """
        Raises an error if the desired llm model is not supported yet.
        """
        self.logger.log_error(f"The selected LLM model is not supported : {model_name}.")
        raise BasicException(code=500, detail=f"The selected LLM model is not supported.")
    
    def search_api_not_supported_error(self, api_name=""):
        """
        Raises an error if the desired search api is not supprted yet.
        """
        self.logger.log_error(f"The selected search api is not supported : {api_name}.")
        raise BasicException(code=500, detail=f"The selected search api is not supported.")

    def research_error(self):
        """
        Raises an error when the research failed
        """
        self.logger.log_error(f"The research in the research API failed.")
        raise BasicException(code=500, detail=f"The research in the research API failed.")
    