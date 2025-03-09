"""
Interface for our application : lets the user specify which theme he wants to do research on and displays the summary of said research.
"""

from dotenv import load_dotenv
import json
import os

from api_client.api_client import APIClient
from utils.error_handler import ErrorHandler
from front.interface_client import InterFaceClient

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")

api_client = APIClient(API_BASE_URL, API_KEY)
error_handler = ErrorHandler()
interface_client = InterFaceClient()


def logout():
    print("test")

def main():
    # TODO : authentication of users

    interface_client.config_page_favicon("Assistant veille 🔎", 'assets/img/research.png')
    
    # Generate sidebar
    interface_client.generate_sidebar(
        "assets/img/research.png", 
        "Welcome! What topic do you want to explore?", 
        "Choose which LLM you want to use.")
    llm_choice = interface_client.add_radio_button_in_sidebar("Select which LLM to choose", ["openai", "mistral", "azure openai"], ["", "", ""])
    interface_client.add_button_to_sidebar("log out →", logout)

    # Get user query
    interface_client.generate_title("LLM-Augmented search bar 🔎")
    user_query, validate_form = interface_client.generate_query_box(
        "llm_query",
        "On which topic would you want to do some research?",
        'Enter a topic or a question on which you want to know more.',
        "Submit")

    # Do research
    if validate_form:
        api_results = interface_client.wait_for_action(
            api_client.call_api, 
            action_text="Searching the internet...", 
            resolution_text="Search Successful", 
            headers={}, 
            content={"topic" : user_query, "llm_type" : llm_choice, "search_type": "serpapi"}, 
            endpoint="research")
    
        ## Display
        if api_results.status_code != 200:
            error_handler.api_error(api_results)
        results_list = json.loads(api_results.content.decode())["response"]
        print(results_list)
        if len(results_list) == 0:
            error_handler.empty_results(user_query)
        else:
            for my_result in results_list:
                interface_client.display_result_value(
                    title=my_result["extracted_page"]["title"], 
                    url=my_result["url"], 
                    date=my_result["extracted_page"]["date"], 
                    content=my_result["extracted_page"]["summary"], 
                    website=my_result["extracted_page"]["website_name"])
                

if __name__ == "__main__":
    main()
