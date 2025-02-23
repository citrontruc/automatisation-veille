"""
A class to create an llm client that can interact with a mistral model
"""
from langchain_mistralai import ChatMistralAI

from llm_client import LLMClient


class MistralClient(LLMClient):
    """
    Inherits from LLMClient. Redefines methods to call the model with the appropriate Mistral credentials
    """
    def _create_llm(self):
        """
        Creates and configures our LLM.
        """
        return ChatMistralAI(
                api_key=self.credentials,
                model="mistral-small-latest",
                max_tokens=2048,
                seed=42,
                temperature=0,
                top_p = 0
            )
