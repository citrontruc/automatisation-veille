"""
A class to create an llm client that can interact with an openai model
"""
from langchain_openai import ChatOpenAI

from src.llm.llm_client.llm_client import LLMClient


class OpenAIClient(LLMClient):
    """
    Inherits from LLMClient. Redefines methods to call the model with the appropriate OpenAI credentials
    """    
    def _create_llm(self):
        """
        Creates and configures our LLM.
        """
        return ChatOpenAI(
                api_key=self.credentials,
                model="gpt-4o-mini",
                max_tokens=2048,
                seed=42,
                temperature=0,
                top_p=0
            )
