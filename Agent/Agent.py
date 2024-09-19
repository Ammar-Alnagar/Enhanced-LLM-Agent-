from langchain import OpenAI, LLMChain
from langchain.agents import AgentExecutor, LLMSingleActionAgent
from agent.prompt import CustomPromptTemplate
from agent.output_parser import CustomOutputParser
from tools.search_tools import DuckDuckGoSearchRun, WikipediaQueryRun
from tools.math_tools import WolframAlphaRun, PythonREPLTool
from tools.language_tools import TextTranslationTool, SentimentAnalysisTool
from tools.misc_tools import WeatherTool, NewsAPITool

def create_agent_executor():
    llm = OpenAI(temperature=0)

    tools = [
        DuckDuckGoSearchRun(),
        WikipediaQueryRun(),
        WolframAlphaRun(),
        PythonREPLTool(),
        TextTranslationTool(),
        SentimentAnalysisTool(),
        WeatherTool(),
        NewsAPITool(),
    ]

    prompt = CustomPromptTemplate(
        template=CustomPromptTemplate.template,
        tools=tools,
        input_variables=["input", "agent_scratchpad"]
    )

    output_parser = CustomOutputParser()
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    agent = LLMSingleActionAgent(
        llm_chain=llm_chain,
        output_parser=output_parser,
        stop=["\nObservation:"],
        allowed_tools=[tool.name for tool in tools]
    )

    return AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
