"""
A class to handle the interactions between our API and our LLMClient
"""
from langchain_core.output_parsers import JsonOutputParser

from llm_client.azure_openai_client import AzureOpenAIClient
from llm_client.mistral_client import MistralClient
from llm_client.openai_client import OpenAIClient
from ..schemas.llm.llm_template import SummaryTemplate


class LLMClient:
    """
    A class to handle the interactions between our API and our LLMClient
    """
    def __init__(self, llm_type, credentials, endpoint="", deployment_id="", api_version=""):
        match llm_type:
            case "azure openai":
                self.llm_client = AzureOpenAIClient(credentials, endpoint, deployment_id, api_version)
            case "mistral":
                self.llm_client = MistralClient(credentials)
            case "openai":
                self.llm_client = OpenAIClient(credentials)
            case _:
                print("error")
    
    def ask_llm(self, prompt, system_prompt=""):
        """
        A method to ask an llm a query
        input:
            prompt (str)
            system_prompt (str)
        output:
            (str)
        """
        llm_response = self.llm_client.ask(prompt, system_prompt)
        return llm_response.content
    
    def ask_llm_structured(self, prompt, system_prompt, answer_schema):
        """
        A method to ask an llm a query and get a structured output
        input:
            prompt (str)
            system_prompt (str)
            answer_schema (class)
        output:
            (dict)
        """
        return self.llm_client.ask_structured(prompt, system_prompt, answer_schema)
    
    def summarize_document(self, document_dict):
        """
        A method to summarize a document
        input:
            document_dict (dict)
        output:
            (dict)
        """
        template_parser = JsonOutputParser(pydantic_object=SummaryTemplate)
        prompt = f"""Here is the dictionary of documents to summarize : {document_dict}.
        Don't forget, your answer should have the following form : {template_parser.get_format_instructions()}."""
        system_prompt = f"""You are a summarizer. Your role is to extract the key information from a list of sources.
        For each of these sources, give an individual summary with some key information, then give a global summary of all the documents.
        Your answers should have the following form : {template_parser.get_format_instructions()}."""
        return self.ask_llm_structured(prompt, system_prompt, SummaryTemplate)
