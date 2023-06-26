import sqlite3

class BotDBService:
    def __init__(self, db_path):
        """
        Initializes the BotDBService with the specified SQLite database path.

        Args:
            db_path (str): The path to the SQLite database file.
        """
        # Establish a connection to the SQLite database
        self.connection = sqlite3.connect(db_path)

    def create_tables(self):
        """
        Creates the necessary tables in the database if they don't exist.
        """
        # Execute SQL statements to create the required tables in the database

    def insert_message(self, message):
        """
        Inserts a message into the message history table.

        Args:
            message (str): The message to be inserted.
        """
        # Insert the message into the message history table in the database

    def get_message_history(self):
        """
        Retrieves the entire message history from the database.

        Returns:
            list: A list of messages in the message history.
        """
        # Fetch the entire message history from the message history table in the database

    def clear_message_history(self):
        """
        Clears the message history by deleting all records from the message history table.
        """
        # Delete all records from the message history table in the database

    def update_language_setting(self, user_id, language):
        """
        Updates the language setting for a specific user.

        Args:
            user_id (str): The ID of the user.
            language (str): The new language setting for the user.
        """
        # Update the language setting for the specified user in the settings table

    def get_language_setting(self, user_id):
        """
        Retrieves the language setting for a specific user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The language setting for the user.
        """
        # Fetch the language setting for the specified user from the settings table

    def close_connection(self):
        """
        Closes the connection to the SQLite database.
        """
        # Close the connection to the SQLite database
