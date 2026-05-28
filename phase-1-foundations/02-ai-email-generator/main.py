from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.email_generator import EmailGenerator
from app.schemas import EmailRequest
from app.utils import format_response

app = FastAPI(
    title="AI Email Generator",
    description="Generate professional emails using AI",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    """
    Health check
    :return: Health check status
    """
    return {
        "status": "healthy"
    }


@app.post("/generate-email")
def generate_email(email_request: EmailRequest):
    """
    Generate professional email
    :param email_request: Email request
    :return: JSON response if email is generated successfully if exception then error response
    """
    try:
        generated_email = EmailGenerator.generate_email(email_request)

        return JSONResponse(
            status_code=200,
            content=format_response(generated_email)
        )

    except Exception as error:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(error)
            }
        )
