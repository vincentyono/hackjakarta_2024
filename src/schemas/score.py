from langchain.pydantic_v1 import BaseModel, Field

class Score(BaseModel):
    """
    You are an expert software engineer with 20 years of experience.
    you are given a task to write an optimized code with the same purpose of
    the given code.
    """

    error_possibility: int = Field("from scale of 0 to 100, how likely is it going to have an unexpected output?")
    understandability: int = Field("from scale of 0 to 100, how easy it is to understand?")
    maintainability: int = Field("from scale of 0 to 100, how maintainable is the code?")
    modularization: int = Field("from scale of 0 to 100, how modularized is the code?")
    cyclomatic_complexity: int = Field("what is the cyclomatic complexity of the code?")
