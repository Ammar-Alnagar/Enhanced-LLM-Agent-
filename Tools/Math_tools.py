from langchain.tools import WolframAlphaQueryRun, PythonREPLTool as BasePythonREPLTool

class WolframAlphaRun(WolframAlphaQueryRun):
    name = "Wolfram Alpha"
    description = "Use Wolfram Alpha for complex calculations and queries"

class PythonREPLTool(BasePythonREPLTool):
    name = "Python REPL"
    description = "Execute Python code and return the result"
