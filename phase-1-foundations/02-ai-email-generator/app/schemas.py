from typing import List

from pydantic import BaseModel


class EmailRequest(BaseModel):
    """
    Email request model
    """
    purpose: str
    tone: str
    recipient: str
    key_points: List[str]


class EmailResponse(BaseModel):
    """
    Email response model
    """
    generated_email: str
