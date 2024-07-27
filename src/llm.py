from settings import get_settings
from langchain_openai import ChatOpenAI
from schemas import Suggestion, Score

class LLM:
    def __init__(self):
        self.__model = get_settings().openai_model
        self.__api_key = get_settings().openai_api_key
        self.chat = ChatOpenAI(
            model=self.__model,
            api_key=self.__api_key,
            temperature=0
        )

    def code_variation(self, code: str):
        structured_output = self.chat.with_structured_output(Suggestion)
        return structured_output.invoke(code)

    def code_scoring(self, code: str):
        structured_output = self.chat.with_structured_output(Score)
        return structured_output.invoke(code)