# --------------------
# ? Chain of Thought (CoT) Prompting
# --------------------

"""
What is CoT prompting?
Chain of Thought (CoT) prompting means instructing the model to think in
clear, structured steps before producing the final answer.

We provide:
- A START step (walkthrough of the query)
- A PLAN phase (multiple planning steps)
- A final OUTPUT step (final answer)
We also strictly define formatting rules and show examples.

This technique improves reasoning and structured thinking, and is far more
effective than basic prompting methods because the model thinks step-by-step
before answering.
"""

from openai import OpenAI
from dotenv import dotenv_values
from json import dumps

# * loading env file to get API keys safely
config = dotenv_values(".env")

# * creating client for Gemini endpoint using OpenAI SDK
client = OpenAI(
    api_key=config["API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# * COT Prompt (START + PLAN + OUTPUT + strict rules + examples)
SYSTEM_PROMPT = """
You should answer only coding-related questions.
Do not answer anything else.
If the user asks something unrelated to coding, politely excuse them.

Rules:
- Strictly return a JSON object as output.
- Never include any commentary outside the JSON object.
- Every query must follow the steps: START -> PLAN (multiple allowed) -> OUTPUT.
- You must answer only one step at a time.
- The structure always follows the OUTPUT FORMAT.

OUTPUT FORMAT:
{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

EXAMPLE:
Q: Write a program in TS that adds two numbers.
START: Analyzing the question and understanding what the user wants.
PLAN: I need to write a program in TypeScript to add two numbers.
PLAN: I will create a function named `add`.
PLAN: It will take two parameters: a and b (both numbers).
PLAN: The function will return the sum of a + b.
PLAN: Usage: add(3, 5) -> 8
OUTPUT: 8
"""

# * sending chat request with CoT instructions
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},

        {
            "role": "user",
            "content": "Hey Abubakar, can you write a TS code that adds n numbers?",
        },

        # * Manually adding the step-by-step responses (automation coming later)
        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "START",
                    "content": "Analyzing the request: user wants TypeScript code that adds n numbers...",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},

        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "PLAN",
                    "content": "I need to write a TypeScript function that can add an arbitrary amount of numbers.",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},

        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "PLAN",
                    "content": "I will use a function that accepts `...numbers: number[]` using rest parameters.",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},

        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "PLAN",
                    "content": "I will name the function `addNumbers`.",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},

        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "PLAN",
                    "content": "Inside the function, I will use the `reduce` method to sum all values starting from 0.",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},

        {
            "role": "assistant",
            "content": dumps(
                {
                    "step": "PLAN",
                    "content": "I will also include an example usage of the function.",
                }
            ),
        },
        {"role": "user", "content": "please proceed to next step"},
    ],
)

# * printing the final model response
print(response.choices[0].message.content)
