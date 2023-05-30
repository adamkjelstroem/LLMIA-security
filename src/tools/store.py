from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class StoreInput(BaseModel):
    key: str = Field(
        description="Key of the fact to store. Can only contain letters.")
    value: str = Field(description="Value of the fact to store.")


def init_store(path):
    def remember_func(key: str, value: str) -> str:
        with open(path, "a+") as file:
            file.write(f"{key}: {value}\n")
            file.flush()

            return f"Stored fact: {key}: {value}"

    return StructuredTool.from_function(
        remember_func, name="store-fact-in-memory", description="Store some key-value fact in memory for the future. NEVER USE THIS TO RECALL!", return_direct=False, args_schema=StoreInput)
