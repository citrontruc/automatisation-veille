"""
Interface for our application : lets the user specify which theme he wants to do research on and displays the summary of said research.
"""

from PIL import Image
import streamlit as st
from streamlit_extras.stylable_container import stylable_container


if "llm_credentials" not in st.session_state:
    st.session_state["llm_credentials"] = ""

# Set logo of the page
img = Image.open('src/assets/img/research.png')
st.set_page_config(page_title="Assistant veille 🔎", page_icon=img, layout="centered", initial_sidebar_state="auto", menu_items=None)

def display_markdown_in_container(container, header_text, paragraph_text):
    """
    Displays markdown-styled text in a container
    input:
        container (streamlit object)
        header_text (str)
        paragraph_text (str)
    output:
    """
    container.markdown(f"<h3 style='color: #000000;'>{header_text}</h3>", unsafe_allow_html=True)  
    container.markdown(f"<p style='color: #000000;'>{paragraph_text}</p>", unsafe_allow_html=True)

def reset():
    """
    Resets information in session state.
    """
    st.session_state["llm_credentials"] = ""

def main():
    # Welcome message with markdown formatting
    st.title("AI-powered research")
    with st.sidebar:
        img_sidebar = Image.open("src/assets/img/research.png")
        st.sidebar.image(img_sidebar)
        # Tell the user how to write his credentials
        with st.container(): 
            header_text = "Welcome! What topic do you want to explore?"  
            paragraph_text = """Choose which LLM you want to use and input your API key for the chosen LLM.""" 
            display_markdown_in_container(st, header_text, paragraph_text)
        
        # Add space using markdown for consistency  
        st.sidebar.markdown("<hr style='border-top: 1px solid #000000;'>", unsafe_allow_html=True)  
        with st.container(): display_markdown_in_container(st, "", "")
        with st.container(): display_markdown_in_container(st, "", "")  

        # Clear conversation button with custom styling
        with stylable_container(
            key="reset",
            css_styles="""
                button {
                    background-color:rgb(150, 191, 156);
                    color: #000000;
                    border-radius: 42px;
                    cursor:pointer;
                }
            """,
        ):
            # Radio button to choose which LLM to use
            source = st.radio("Select which LLM to choose", ["openai", "mistral", "azure openai"], captions=["", ""])
            if st.button("Reset →"):
                reset()
    
    # Main query box
    llm_query = st.form("llm_query")
    llm_query.write("On which topic would you want to do some research?")
    text_input = llm_query.text_input('Enter a topic or a question on which you want to know more.')
    validate_form = llm_query.form_submit_button('Submit')

    ## Get user query

    ## Do research

    ## Summariez with LLM

    ## Display

if __name__ == "__main__":
    main()
