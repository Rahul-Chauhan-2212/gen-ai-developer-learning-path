from openai import OpenAI
from rich.console import Console

from .config import OPENAI_API_KEY, MODEL_NAME
from .prompts import SYSTEM_PROMPT

console = Console()


class AIChatbot:
    """
    AI Chatbot Class which is used to Call Open AI APIs with respective message which is combination of System and User Prompt
    """

    def __init__(self):
        """
        Initialization function
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY)

        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

    def chat(self, user_input: str):
        """
        Chatbot function
        :param user_input: User Input
        :return: LLM Response
        """
        self.messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.messages,
            temperature=0.7,  # Tune LLM predictability, creativeness and randomness
        )

        assistant_reply = response.choices[0].message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_reply,
            }
        )

        return assistant_reply
