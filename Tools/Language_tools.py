from langchain.tools import BaseTool
from textblob import TextBlob
from googletrans import Translator

class TextTranslationTool(BaseTool):
    name = "Text Translator"
    description = "Translate text from one language to another"

    def _run(self, query: str) -> str:
        translator = Translator()
        result = translator.translate(query)
        return f"Translated from {result.src} to {result.dest}: {result.text}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("TextTranslationTool does not support async")

class SentimentAnalysisTool(BaseTool):
    name = "Sentiment Analyzer"
    description = "Analyze the sentiment of a given text"

    def _run(self, query: str) -> str:
        blob = TextBlob(query)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            return f"Positive sentiment (score: {sentiment})"
        elif sentiment < 0:
            return f"Negative sentiment (score: {sentiment})"
        else:
            return f"Neutral sentiment (score: {sentiment})"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("SentimentAnalysisTool does not support async")
