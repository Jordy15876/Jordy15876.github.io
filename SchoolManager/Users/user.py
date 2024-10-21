class User:
    def __init__(self, username, password):
        """Initialize a User object with a username and password.

        Args:
            username (str): The user's unique username.
            password (str): The user's password for authentication.
        """
        self.username = username
        self.password = password

    def authenticate(self, username, password):
        """Verify that the provided username and password match the stored credentials.

        This method checks whether the username and password supplied by the user
        correspond to the credentials stored for this user instance.

        Args:
            username (str): The username to authenticate.
            password (str): The password provided for authentication.

        Returns:
            bool: True if both the username and password match the stored credentials, False otherwise.
        """
        return self.username == username and self.password == password
