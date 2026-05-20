import unittest

from app.chatbot import AIChatbot

class TestChatbot(unittest.TestCase):

    def test_chatbot_initialization(self):
        chatbot = AIChatbot()

        self.assertIsNotNone(chatbot)


if __name__ == "__main__":
    unittest.main()
