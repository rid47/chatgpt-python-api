from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
load_dotenv()


class CodeOutput(BaseModel):
    function_name: str
    code: str
    explanation: str
    example_usage: str

user_input = input("Describe the python function you want help with: ")


client = OpenAI()

code_response = client.responses.parse(
    model="gpt-5",
    input=[
        {
            "role": "developer",
            "content": (
                "You are a Python coding assitant."
                "Only accept Python-related questions."
            ),
        },
        {
            "role": "user",
            "content": f"{user_input}"
        }
    ],

    text_format=CodeOutput,
)


code_result: CodeOutput = code_response.output_parsed


print(f"Function: {code_result.function_name}")
print(f"Code:\n{code_result.code}")
print(f"Explanation: {code_result.explanation}")
print(f"Example Usage: {code_result.example_usage}")
