"""
An object to check user credentials depending on authentication method
"""

class Authenticator:
    """
    A parent class that can be used to check user credentials (TODO)
    """
    def __init__(self):
        pass

    def check_key_simple(self, input_key):
        """
        Check if the input key corresponds to the 
        input:
            input_key (str)
        output:
            Boolean
        """
