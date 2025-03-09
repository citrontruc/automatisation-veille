"""
An object to identify the user with Azure or GCP using streamlit oauth.
"""

from dotenv import load_dotenv
import os
import re
import requests
from streamlit_oauth import OAuth2Component

load_dotenv()

class AuthenticationClient:
    """
    An object to check the credentials of the user.
    """
    def __init__(self) -> None:
        self.AUTHORIZE_URL =  os.environ.get("AUTHORIZE_URL")
        self.TOKEN_URL =  os.environ.get("TOKEN_URL")
        self.REFRESH_TOKEN_URL =  os.environ.get("REFRESH_TOKEN_URL")
        self.REVOKE_TOKEN_URL =  os.environ.get("REVOKE_TOKEN_URL")
        self.CLIENT_ID =  os.environ.get("CLIENT_ID")
        self.TENANT_ID =  os.environ.get("TENANT_ID")
        self.CLIENT_SECRET =  os.environ.get("CLIENT_SECRET")
        self.REDIRECT_URI =  os.environ.get("REDIRECT_URI")
        self.SCOPE =  os.environ.get("SCOPE")
        self.API_URL =  os.environ.get("API_URL") or 'http://api'
        self.USER_INFO_URL = os.environ.get("USER_INFO_URL")
        self.GROUP_USER = os.environ.get("GROUP_USER") or ""
        self.oauth2 = OAuth2Component(
                self.CLIENT_ID,
                self.CLIENT_SECRET,
                self.AUTHORIZE_URL,
                self.TOKEN_URL,
                self.REFRESH_TOKEN_URL,
                self.REVOKE_TOKEN_URL
            )
        
    def create_login_button(self):
        """
        Creates a button for the user to log in.

        no input
        
        output:
            (streamlit button)
        """
        return self.oauth2.authorize_button("Log in", self.REDIRECT_URI, self.SCOPE)
    
    def check_user_credentials(self, result):
        """
        Checks if the user has an access token and if his mail corresponds to the accepted mails.

        input:
            result (dict)

        output:
            login_accepted (bool)
            token (str)
            mail (str)
        """
        headers = {
                'Authorization': 'Bearer ' + result['token']['access_token'],
            }
        
        try:
            user = requests.get(self.USER_INFO_URL, headers = headers).json()
            if self.GROUP_USER != "":
                has_acccess_to_group = self.check_group_access(user, headers)
                if not has_acccess_to_group:
                    return False, None, None
                else:
                    return True, result['token'], user['mail']
        except:
            return False, None, None
        # Azure and GCP don't use the same term to designate mail (one uses mail and the other email)
        # Regex to check patterns in the mail in case we have multiple populations
        match = re.compile(
                r'^.+?@gmail\.com$',
                flags=re.IGNORECASE
            )
        if 'email' in user:
            if not match.match(user['email']):
                return False, None, None
            return True, result['token'], user['email']
        if 'mail' in user:
            if not match.match(user['mail']):
                return False, None, None
            return True, result['token'], user['mail']
    
    def check_group_access(self, user, headers):
        """
        Checks if the user is part of a given microsoft group.
            
        input:
            user (dict)
            headers (dict)

        output:
            (bool)
        """
        url = f"https://graph.microsoft.com/v1.0/users/{user['id']}/memberOf"
        all_group = requests.get(url, headers = headers).json()
        for group in all_group["value"]:
            if group["id"] == self.GROUP_USER:
                return True
        return False
