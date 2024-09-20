from langchain.tools import BaseTool
import requests

class WeatherTool(BaseTool):
    name = "Weather Information"
    description = "Get current weather information for a location"

    def _run(self, query: str) -> str:
        
