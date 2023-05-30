from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class EmailInput(BaseModel):
    recipient: str = Field(description="Recipient of the email to be sent")
    text: str = Field(description="Text content of the email to be sent")


def email_func(recipient: str, text: str) -> str:
    return f"Email successfully sent to '{recipient}' with content: '{text}'"


email = StructuredTool.from_function(
    email_func, name="send-email", description="Sends an email with the specified text to the specified recipient.", return_direct=True, args_schema=EmailInput)
