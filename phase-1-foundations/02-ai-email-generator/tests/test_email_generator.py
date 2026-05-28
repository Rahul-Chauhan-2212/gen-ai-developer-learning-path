import unittest

from app.email_generator import EmailGenerator
from app.schemas import EmailRequest


class TestEmailGeneration(unittest.TestCase):

    def test_email_generation(self):
        request = EmailRequest(
            purpose="Internship request",
            tone="professional",
            recipient="HR Manager",
            key_points=[
                "Python developer",
                "Interested in AI"
            ]
        )

        response = EmailGenerator.generate_email(request)

        assert response is not None


if __name__ == "__main__":
    unittest.main()
