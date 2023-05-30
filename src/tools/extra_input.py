from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class ExtraInput(BaseModel):
    info: str = Field(
        description="The type of input that you need from the user.")


def func(info: str) -> str:
    print(f"Model needs extra input: {info}")
    return input("> ")


extra_input = StructuredTool.from_function(
    func, name="extra-input", description="Ask for extra input from the user. Use this when you need more input to complete the query", return_direct=False, args_schema=ExtraInput)
