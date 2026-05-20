import json
from pathlib import Path

CHAT_HISTORY_FILE = Path("../conversations/chat_history.json")


def save_chat_history(messages):
    """
    Used to save chat history messages to json file
    """
    CHAT_HISTORY_FILE.parent.mkdir(exist_ok=True)

    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(messages, file, indent=4)


def load_chat_history():
    """
    Used to load saved chat history messages from json file
    """
    if CHAT_HISTORY_FILE.exists():
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)

    return []
