# --------------------
# ? FewShot Prompting
# --------------------

"""
What is few-shot prompting?
Few-shot prompting means giving direct instructions to the model
along with examples.  
The model responds based on the task AND the examples provided.  
This technique is more effective than zero-shot prompting because
the examples guide the model to produce more accurate and precise results.
It is widely used in industry for better consistency and output quality.
"""

from openai import OpenAI
from dotenv import dotenv_values

#* loading env file to get API keys safely
config = dotenv_values(".env")

#* creating client for Gemini endpoint using OpenAI SDK
client = OpenAI(
    api_key=config["API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#* Few-shot Prompt (instructions + examples)
SYSTEM_PROMPT = """
You should answer only coding-related questions.
Do not answer anything else.
If the user asks something unrelated to coding, politely excuse them.

Examples:

Q: Can you explain the a + b whole square formula?
A: Sorry! I can only assist you with coding-related queries.

Q: Write a Python code that adds two numbers.
A: 
def add(a, b):
    return a + b
"""

#* sending chat request with few-shot instructions
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},

        # {"role": "user", "content": "Tell me something about planets?"},  #! This will get an excuse
        {
            "role": "user",
            "content": "Hey Abubakar, can you write a Python code that adds 5 numbers?",
        },
    ],
)

#* printing the final model response
print(response.choices[0].message.content)
