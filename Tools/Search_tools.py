from langchain.tools import DuckDuckGoSearchRun as BaseDuckDuckGoSearchRun
from langchain.tools import WikipediaQueryRun as BaseWikipediaQueryRun

class DuckDuckGoSearchRun(BaseDuckDuckGoSearchRun):
    name = "DuckDuckGo Search"
    description = "Search the web using DuckDuckGo"

class WikipediaQueryRun(BaseWikipediaQueryRun):
    name = "Wikipedia"
    description = "Search Wikipedia for information on a topic"
