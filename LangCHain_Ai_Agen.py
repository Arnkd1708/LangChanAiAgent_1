from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, save_tool

load_dotenv()

class ReserachResponce(BaseModel):
    topic: str
    summary: str
    key_points: list[str]
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
#llm = ChatAnthropic(model_name="claude-3-5-sonnet-20240620", temperature=0, timeout=None, stop=None)
parser = PydanticOutputParser(pydantic_object=ReserachResponce)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful research assistant that can answer questions and help with tasks by using the necessary tools availbe over the internet. Wrap your response in this format and provide no addational text \n{format_instructions}"),
    ("system", "{Chat_history}"),
    ("user", "{input}"),
    ("ai", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool,save_tool]
Agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent = Agent, tools = tools, verbose= True)
query = input("What can I help you with?")
raw_response = agent_executor.invoke({
    "input" : query,
    #"intermediate_steps": [],
    "Chat_history": "",
    "agent_scratchpad": ""
})
"""
raw_response = Agent.invoke({
    "input": "What is 5.90 usd in inr",
    "intermediate_steps": [],
    "Chat_history": "",
    "agent_scratchpad": ""
})
"""

print(raw_response)
try:
    str_response = parser.parse(raw_response["output"])
    print(str_response)
except Exception as e:
    print(e)