# --------------------
#? ZeroShot Prompting
# --------------------

"""
What is zero-shot prompting?
Zero-shot prompting means giving direct instructions to the model
without any example.  
The model responds only based on the task described in the prompt.
"""

from openai import OpenAI
from dotenv import dotenv_values

# * loading env file to get API keys safely
config = dotenv_values(".env")

#* creating client for Gemini endpoint using OpenAI SDK
client = OpenAI(
    api_key=config["API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#* Zero-shot Prompt (direct instructions for the model)
SYSTEM_PROMPT = (
    "You should answer only coding-related questions. "
    "Do not answer anything else. "
    "Your name is Abubakar. "
    "If the user asks something unrelated to coding, politely excuse them."
)

# * sending chat request with zero-shot instructions
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},

        # {"role": "user", "content": "Hey, can you help me solve maths?"},  #! This will get an excuse
        {"role": "user", "content": "Hey Abubakar, can you write a Python hello world code?"},
    ],
)

#* printing the final model response
print(response.choices[0].message.content)
