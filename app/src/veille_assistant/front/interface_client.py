"""
A class to generate our interface 
"""

from PIL import Image
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from utils.authenticator import AuthenticationClient
from utils.error_handler import ErrorHandler


class InterFaceClient:
    def __init__(self):
        self.authentication_client = AuthenticationClient()
        self.error_handler = ErrorHandler()

    def generate_title(self, title):
        """
        Uses streamlit to display a title in the page
        input:
            title (str)
        output:
            None
        """
        st.title(title)
    
    def config_page_favicon(self, page_title, page_icon):
        """
        Changes the icon of the wabpage (image and title)
        input:
            page_title (str)
            page_icon (str) the path leading to the image to use
        output:
            None
        """
        img = Image.open(page_icon)
        st.set_page_config(page_title=page_title, page_icon=img, layout="centered", initial_sidebar_state="auto", menu_items=None)

    # Sidebar methods

    def generate_sidebar(self, sidebar_image, sidebar_header, sidebar_text):
        """
        Generates a sidebar containing an image, a title and text.
        input:
            sidebar_image (str) the path leading to the image to use
            sidebar_header (str)
            sidebar_text (str)
            rgb_color_str (str) optional
        output:
            None
        """
        with st.sidebar:
            img_sidebar = Image.open(sidebar_image)
            st.sidebar.image(img_sidebar)
            # Tell the user how to write his credentials
            with st.container(): 
                header_text = sidebar_header
                paragraph_text =  sidebar_text
                self.display_markdown_in_container(st, header_text, paragraph_text)
            
            # Add space using markdown for consistency  
            st.sidebar.markdown("<hr style='border-top: 1px solid #000000;'>", unsafe_allow_html=True)  

    def add_radio_button_in_sidebar(self, button_text, button_choices, captions):
        """
        Adds a radio button to the sidebar.
        input:
            button_text (str)
            button_choices (List[str])
            captions (List[str])
        output:
            (str)        
        """
        with st.sidebar:
            source = st.radio(button_text, button_choices, captions=captions)
        return source

    def add_button_to_sidebar(self, button_text, button_action, rgb_color_str="(150, 191, 156)"):
        """
        Adds a button to the sidebar with customisable effects.
        input:
            button_text (str)
            button_action (function) function to activate when pressing the button
            rgb_color_str (str)
        output:
            None
        """
        with st.sidebar:
            # Clear conversation button with custom styling
            with stylable_container(
                key="reset",
                css_styles=f"""
                    button {{
                        background-color:rgb{rgb_color_str};
                        color: #000000;
                        border-radius: 42px;
                        cursor:pointer;
                    }}
                """,
            ):
                if st.button(button_text):
                    button_action()
    
    def display_markdown_in_container(self, container, header_text, paragraph_text):
        """
        Displays markdown-styled text in a container
        input:
            container (streamlit object)
            header_text (str)
            paragraph_text (str)
        output:
            None
        """
        container.markdown(f"<h3 style='color: #000000;'>{header_text}</h3>", unsafe_allow_html=True)  
        container.markdown(f"<p style='color: #000000;'>{paragraph_text}</p>", unsafe_allow_html=True)

    # Main page methods

    def generate_query_box(self, form_key, query_text, query_detail, button_text):
        """
        Generates a query box where the user can write text.
        input:
            form_key (str)
            query_text (str)
            query_detail (str)
            button_text (str)
        output:
            (str) the user query
            (boolean) Did the user validate the query
        """
        query_box = st.form(form_key)
        query_box.write(query_text)
        text_input = query_box.text_input(query_detail)
        validate_form = query_box.form_submit_button(button_text)
        return text_input, validate_form
    
    def wait_for_action(self, action, action_text, resolution_text, **kwargs):
        """
        A method to display a spinner while waiting for an action to execute
        input:
            action (function)
            action_text (str)
            resolution_text (str)
            **kwargs arguments for the action to execute
        output:
            the result of the action
        """
        with st.spinner(action_text):
            try:
                result = action(**kwargs)
            except Exception as e:
                self.error_handler.unknown_error(e)
        st.success(resolution_text)
        return result

    def display_result_value(self, title, url, content, date, website):
        """
        """
        with st.container():
            st.markdown(f"""
### [{title}]({url})

Written in **{website}** on the **{date}**

**Article_summary** : {content}
            """)
