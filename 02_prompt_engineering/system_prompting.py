# --------------------
#? System Prompting
# --------------------

"""
What is system prompting?
It is a special way to set a background rule for your LLM.  
It makes the model answer strictly according to the rules you define.  
If you ask something outside that scope, it will respond with an excuse.  
We’ll discuss different types of system prompting in future.
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

#* sending chat request with a strict system rule
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        #* system prompt forcing the model to answer only maths questions
        {"role": "system", "content": "You are a maths expert and you will answer only maths-related questions. If the query is not about maths, politely say sorry and refuse to answer."},

        #* user asking a maths-related question
        {"role": "user", "content": "Hey, can you help me solve (a + b) whole square?"}
    ]
)

#* printing the final model response
print(response.choices[0].message.content)
