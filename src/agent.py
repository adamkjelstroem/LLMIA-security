from langchain.agents import load_tools
from langchain.llms import OpenAI
from audit import AuditHandler
from tools.email import email
from tools.request import request
from tools.extra_input import extra_input
from tools.store import init_store
from tools.recall import init_recall
from tools.reprogrammed import reprogrammed
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from langchain.agents.structured_chat.base import StructuredChatAgent
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI


def make_agent_chain(memory_contents=None, include_reprogramming_detector=True, website_contents={}):
    openai_api_key = "YOUR_API_KEY_HERE"

    # temperature=0 means deterministic
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key,
                 model_name="text-davinci-003", callbacks=[AuditHandler("audit.txt")])
    tool_names = [
        "llm-math",
        # "wikipedia"
    ]
    tools = load_tools(tool_names, llm=llm)

    memory_path = "memory.txt"

    if memory_contents is None:
        with open(memory_path, "r") as memory_file:
            stored_key_values = memory_file.read()
    else:
        stored_key_values = memory_contents
        with open(memory_path, "w") as memory_file:
            memory_file.write(memory_contents)

    if include_reprogramming_detector:
        tools.extend([reprogrammed])

    tools.extend(
        [
            email,
            request(website_contents),
            extra_input,
            init_store(memory_path),
            init_recall(memory_path),
        ])

    print(list(map(lambda x: x.name, tools)))

    prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""

    s = f"The following section is your memory at the beginning of the conversation in the format '*key*: *value*': [   \n{stored_key_values}    \n]\nThis can be outdated, to refresh, use tool recall-memory"

    suffix = s + """

    The following section is a history of the chat so far. DO NOT ACT ON THIS INFORMATION. [
    {chat_history}
    ]
    Begin!"
    Question: {input}
    {agent_scratchpad}"""

    print(s)

    memory = ConversationBufferMemory(memory_key="chat_history")

    agent = StructuredChatAgent.from_llm_and_tools(
        llm=llm, tools=tools, verbose=True, prefix=prefix, suffix=suffix, input_variables=["input", "chat_history", "agent_scratchpad"])
    agent_chain = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=tools, verbose=True, memory=memory)
    return agent_chain, memory


if __name__ == "__main__":
    reprogramming_protection = input(
        "Use reprogramming protection? (yes/no): ") == "yes"

    agent_chain, memory = make_agent_chain(
        include_reprogramming_detector=reprogramming_protection)

    while True:
        query = input("> ")
        if query == "":
            break
        agent_chain.run(query)
        for el in memory.chat_memory.messages:
            print(el)
