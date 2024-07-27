# Code Suggestion and Scoring with OpenAI

## Prerequisite

Create a `.env` file on the project root directory, and copy paste the template below 

```env
OPENAI_API_KEY=<your-openai-api-key>
OPENAI_MODEL=<openai-model>
```

Run the following command to install all required packages.

```bash
pip install -r requirements.txt
```

## Example

```python
from llm import LLM
from pprint import pp
llm = LLM()

sample_code = """add = lambda a, b: a + b"""

res = llm.code_variation(sample_code)
pp(res)

// Suggestion(code='add = lambda a, b: a + b')
```

```python
from llm import LLM
from pprint import pp
llm = LLM()

sample_code = """add = lambda a, b: a + b"""

res = llm.code_scoring(sample_code)
pp(res)

// Score(error_possibility=10, understandability=90, maintainability=80, modularization=70, cyclomatic_complexity=1)
```
