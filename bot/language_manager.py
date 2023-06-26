import os
import yaml
from bot.translator import Translator

class LanguageManagerService:
    def __init__(self, default_language='en'):
        """
        Initializes the LanguageManagerService with the default language.

        Args:
            default_language (str): The default language code.
        """
        self.default_language = default_language
        self.translator = Translator()

    def load_language_file(self, language_code):
        """
        Loads the language file for the specified language code.

        Args:
            language_code (str): The language code.

        Returns:
            dict: The contents of the language file as a dictionary.
        """
        language_file_path = f"language_files/{language_code}.yml"
        if os.path.exists(language_file_path):
            with open(language_file_path, 'r', encoding='utf-8') as file:
                language_data = yaml.safe_load(file)
            return language_data
        else:
            # If the language file doesn't exist, fall back to default language
            return self.load_language_file(self.default_language)

    def get_translation(self, language_code, key):
        """
        Retrieves the translation for the specified key in the specified language.

        Args:
            language_code (str): The language code.
            key (str): The key to retrieve the translation for.

        Returns:
            str: The translated text.
        """
        language_data = self.load_language_file(language_code)
        translation = language_data.get(key)

        if translation is None:
            # If the translation is not available, fall back to default language
            translation = self.get_translation(self.default_language, key)

        return translation

    def translate_message(self, message, target_language):
        """
        Translates the message to the specified target language.

        Args:
            message (str): The message to be translated.
            target_language (str): The target language code.

        Returns:
            str: The translated message.
        """
        translation = self.translator.translate(message, target_language)
        return translation
