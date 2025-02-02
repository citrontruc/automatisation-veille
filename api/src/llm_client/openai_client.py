"""
A class to create an llm client that can interact with an openai model
"""

from llm_client import LLMClient

class OpenAIClient(LLMClient):
    """
    Inherits from LLMClient. Redefines methods to call the model with the appropriate OpenAI credentials
    """
    def __init__(self):
        super().__init__(self) 
