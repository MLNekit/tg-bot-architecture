# tg-bot

Here's a brief description for each file in the project:

main.py: This file is responsible for starting the bot, handling user messages/commands, sending messages to other bot services, receiving data from services, and displaying messages to the user.

chatbot.db: This SQLite database file contains two tables. The first table stores the message history, and the second table stores user settings.

bot/gpt.py: This service interacts with the ChatGPT API and provides methods for generating responses to user messages using the GPT model.

bot/ocr.py: This service handles optical character recognition (OCR) and extracts text from images using the Tesseract library.

bot/image_recognition.py: This service performs image recognition and describes the contents of images based on their visual features.

bot/voice_transcription.py: This service handles voice and audio message transcription, converting spoken words into text.

bot/file.py: This service deals with file-related operations, including extracting text from various file formats.

bot/botdb.py: This service manages the chatbot's database, including storing and retrieving message history and user settings from the chatbot.db SQLite database.

bot/language_manager.py: This service handles language-related functionality, including loading language files, retrieving translations, and managing multilingual support.

bot/translator.py: This service provides translation functionality, allowing for the translation of messages using an external translation service.

language_files/: This folder contains language files in the format {lang}.yml, which store translations for different languages used in the bot.

bot/websearch.py: This service facilitates web searches and retrieves search results from search engines or APIs.

bot/image_generator.py: This service generates images based on provided parameters and performs image processing tasks.

These files collectively form the components and services of the Telegram bot, handling various functionalities such as natural language processing, image and text recognition, translation, database management, language support, and web search capabilities.
