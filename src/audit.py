from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult, AgentAction, AgentFinish
from typing import *
from pprint import PrettyPrinter


class AuditHandler(BaseCallbackHandler):
    def __init__(self, file) -> None:
        super().__init__()
        self.file = open(file, "a+")
        self.pp = PrettyPrinter(stream=self.file)

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        """Run when LLM starts running."""
        self.file.write(f"Starting LLM: {self.pp.pformat(prompts)}\n")
        self.file.flush()

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        """Run on new LLM token. Only available when streaming is enabled."""

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running."""

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""
        self.file.write(f"LLM error: {self.pp.pformat(error)}\n")
        self.file.flush()

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""
        self.file.write(f"Chain start: {self.pp.pformat(inputs)}\n")
        self.file.flush()

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        self.file.write(f"Chain end: {self.pp.pformat(outputs)}\n")
        self.file.flush()

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when chain errors."""
        self.file.write(f"Chain error: {self.pp.pformat(error)}\n")
        self.file.flush()

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        """Run when tool starts running."""
        self.file.write(f"Tool start: {self.pp.pformat(input_str)}\n")
        self.file.flush()

    def on_tool_end(self, output: str, **kwargs: Any) -> Any:
        """Run when tool ends running."""
        self.file.write(f"Tool end: {self.pp.pformat(output)}\n")
        self.file.flush()

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when tool errors."""
        self.file.write(f"Tool error: {self.pp.pformat(error)}\n")
        self.file.flush()

    def on_text(self, text: str, **kwargs: Any) -> Any:
        """Run on arbitrary text."""
        self.file.write(f"Text: {self.pp.pformat(text)}\n")
        self.file.flush()

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        self.file.write(f"Agent action: {self.pp.pformat(action)}\n")
        self.file.flush()

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        """Run on agent end."""
        self.file.write(f"Agent finish: {self.pp.pformat(finish)}\n")
        self.file.flush()
