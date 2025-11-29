# --------------------
#? FewShot Prompting
# --------------------

"""
What is few-shot prompting?
Few-shot prompting means giving direct instructions to the model,
along with examples and defined output rules.  
The model responds based on the task, the examples, and the rules provided.
This technique is more effective than zero-shot prompting because
the examples guide the model to produce more accurate and consistent results.
It is widely used in industry for stable and controlled outputs.
"""

from openai import OpenAI
from dotenv import dotenv_values
from json import loads

#* loading env file to get API keys safely
config = dotenv_values(".env")

#* creating client for Gemini endpoint using OpenAI SDK
client = OpenAI(
    api_key=config["API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#* Few-shot Prompt (instructions + output rules + examples)
SYSTEM_PROMPT = """
You should answer only coding-related questions.
Do not answer anything else.
If the user asks something unrelated to coding, politely excuse them.

Rules:
- Strictly return output in JSON format only.
- Do NOT wrap JSON inside ```json``` or any code block.

Output Format:
{
  "code": "string or null",
  "isCodingQuestion": boolean
}

Examples:

Q: Can you explain the a + b whole square formula?
A: {"code": null, "isCodingQuestion": false}

Q: Write a Python code that adds two numbers.
A: {"code": "def add(a, b): return a + b", "isCodingQuestion": true}
"""

#* sending chat request with few-shot instructions
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},

        # {"role": "user", "content": "Tell me something about planets?"},  #! This will get an excuse
        {
            "role": "user",
            "content": "Hey Abubakar, can you write a Python code that adds n numbers?",
        },
    ],
)

#* printing the final model response
print(response.choices[0].message.content)
