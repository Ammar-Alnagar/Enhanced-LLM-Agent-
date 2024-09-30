from langchain.prompts import StringPromptTemplate
 
class CustomPromptTemplate(StringPromptTemplate):
    template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:


Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!


Question: {input}
{agent_scratchpad}"""

    def format(self, **kwargs) -> str:
        tools = kwargs.pop("tools")
        kwargs["tool_names"] = ", ".join([tool.name for tool in tools])
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in tools])
        return self.template.format(**kwargs)
