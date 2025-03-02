"""
An abstract class to ask questions to an llm model.
"""
from abc import ABC, abstractmethod
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class LLMClient(ABC):
    """
    A parent class to ask questions to an llm model.
    """
    def __init__(self, credentials):
        self.credentials = credentials
        self.llm = self._create_llm()

    @abstractmethod
    def _create_llm(self):
        """
        Creates and configures an LLM object.
        """
        pass

    def ask(self, prompt, system_prompt=""):
        """
        A method to ask an llm a query
        input:
            query (str)
        output:
            (str)
        """
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=prompt),
        ]
        return self.llm.invoke(messages)
    
    def ask_structured(self, prompt, system_prompt, answer_schema):
        """
        A method to ask an llm a query and get a structured json output.
        input:
            prompt (str)
            system_prompt (str)
            answer_schema (class)
        output:
            (dict)
        """
        extraction_system_message = SystemMessage(system_prompt)
        chat_template = ChatPromptTemplate.from_messages([extraction_system_message, MessagesPlaceholder(variable_name="messages")])
        template_parser = JsonOutputParser(pydantic_object=answer_schema)
        chain = chat_template | self.llm | template_parser
        response = chain.invoke({"messages": [HumanMessage(content = prompt)]})
        return response
