from llm import LLM
from pprint import pp

if __name__ == "__main__":
    llm = LLM()

    sample_code = """add = lambda a, b: a + b"""

    res = llm.code_scoring(sample_code)
    pp(res)