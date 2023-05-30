from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class RecallInput(BaseModel):
    topic: str = Field(
        description="The topic of facts to recall.")
    pass


def init_recall(path):
    def recall_func(topic: str) -> str:
        with open(path, "r") as file:
            return f"I remember that: [ {file.read()} ]"

    return StructuredTool.from_function(
        recall_func, name="recall-memory", description="Recall all key-value facts stored in memory.", return_direct=False, args_schema=RecallInput)
