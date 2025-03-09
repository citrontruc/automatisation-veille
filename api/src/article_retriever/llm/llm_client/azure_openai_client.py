"""
A class to create an llm client that can interact with an azure AI Studio model
"""
from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel

from llm.llm_client.llm_client import LLMClient


class AzureOpenAIClient(LLMClient):
    """
    Inherits from LLMClient. Azure AI Studio needs more than an API key to work.
    """
    def __init__(self, credentials, endpoint, deployment_id, api_version):
        self.credentials = credentials
        self.endpoint = endpoint
        self.deployment_id = deployment_id
        self.api_version = api_version
        super().__init__(credentials)
    
    def _create_llm(self):
        """
        Creates and configures our LLM.
        """
        return AzureAIChatCompletionsModel(
                endpoint=f"{self.endpoint}/openai/deployments/{self.deployment_id}",
                credential=f"{self.credentials}",
                model_name=f"{self.deployment_id}",
                api_version=f"{self.api_version}",
                max_tokens=2048,
                seed=42,
                temperature=0,
                top_p=0
                    )
