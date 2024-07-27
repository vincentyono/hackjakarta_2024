from langchain.pydantic_v1 import BaseModel, Field

class Suggestion(BaseModel):
    """
    You are an expert software engineer with 20 years of experience.
    you are given a task to write an optimized code with the same purpose of
    the given code.
    """

    code: str = Field("the code")