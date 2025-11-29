# --------------------
# ? Auto Chain of Thought (Auto-CoT) Prompting
# --------------------

"""
What is Auto-CoT prompting?
Automatic Chain of Thought (Auto-CoT) prompting means instructing the model to think in
clear, structured steps before producing the final answer.

We provide:
- A START step (walkthrough of the query)
- A PLAN phase (multiple planning steps)
- A final OUTPUT step (final answer)
We also strictly define formatting rules and show examples.
And it auto added new responses

This technique improves reasoning and structured thinking, and is far more
effective than basic prompting methods because the model thinks step-by-step
before answering.
"""

from openai import OpenAI
from dotenv import dotenv_values
import json

# * loading env file to get API keys safely
config = dotenv_values(".env")

# * creating client for Gemini endpoint using OpenAI SDK
client = OpenAI(
    api_key=config["API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# * COT Prompt (START + PLAN + OUTPUT + strict rules + examples)
SYSTEM_PROMPT = """
You should answer in presise manner for user query.
Strictly Obey all rules.

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

print("\n")
message_histroy = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("Enter your query here 👉:  ")
message_histroy.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_histroy,
    )
    raw_result = response.choices[0].message.content
    message_histroy.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print(f"🔥 STARTING: {parsed_result.get("content")}")
        continue
    if parsed_result.get("step") == "PLAN":
        print(f"🧠 THINKING: {parsed_result.get("content")}")
        continue

    if parsed_result.get("step") == "OUTPUT":
        print(f"🤖 RESULT: {parsed_result.get("content")}")
        break


print("\n")