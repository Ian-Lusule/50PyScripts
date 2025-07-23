```python
# simple_chat_bot.py

"""
A simple chat bot using the ChatterBot library.  This bot provides basic responses
based on a predefined knowledge base.  It can be expanded with more training data
for improved conversational abilities.
"""

import logging
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Configure logging to suppress warnings from ChatterBot
logging.basicConfig(level=logging.CRITICAL)

def create_chatbot():
    """Creates and trains a simple chat bot."""

    # Create a new chat bot instance
    chatbot = ChatBot(
        'SimpleChatBot',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, I do not understand.',
                'maximum_similarity_threshold': 0.9
            }
        ],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'  # Use SQLite database
    )


    # Training data -  Expand this for better conversation
    conversation = [
        "Hello",
        "Hi there!",
        "How are you?",
        "I'm doing well, thank you!",
        "What's your name?",
        "I'm a simple chat bot.",
        "What can you do?",
        "I can answer simple questions and have a basic conversation.",
        "Goodbye",
        "Bye!"
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    return chatbot


def main():
    """Main function to run the chat bot."""

    try:
        chatbot = create_chatbot()
        print("Welcome to the Simple Chat Bot!")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chat Bot: Goodbye!")
                break

            response = chatbot.get_response(user_input)
            print("Chat Bot:", response)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

```

To run this code:

1. **Install ChatterBot:**  `pip install chatterbot chatterbot-corpus`
2. **Run the script:** `python simple_chat_bot.py`

The bot will interact with you in the console.  Remember to expand the `conversation` list with more training data for a more robust and engaging experience.  The bot uses an SQLite database to store its knowledge; the database file (`database.sqlite3`) will be created automatically in the same directory as the script.  Error handling is included to catch potential exceptions during chatbot operation.
