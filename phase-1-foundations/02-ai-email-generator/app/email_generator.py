from openai import OpenAI

from .config import OPENAI_API_KEY, MODEL_NAME
from .prompts import SYSTEM_PROMPT
from .schemas import EmailRequest

client = OpenAI(api_key=OPENAI_API_KEY)


class EmailGenerator:

    @staticmethod
    def generate_email(email_request: EmailRequest):
        prompt = f"""
        Generate a professional email.

        Purpose:
        {email_request.purpose}

        Tone:
        {email_request.tone}

        Recipient:
        {email_request.recipient}

        Key Points:
        {", ".join(email_request.key_points)}
        """

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content
