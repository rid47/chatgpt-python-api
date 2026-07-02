from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()



client = OpenAI()

code_response = client.responses.create(
    model="gpt-5",
    input="Please write a simple Python function to add 2 numbers"
)


print(f"Function:\n{code_response.output_text}")


