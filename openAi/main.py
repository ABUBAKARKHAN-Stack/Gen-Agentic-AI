from bytez import Bytez
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

api_key = config["OPEN_AI_API_KEY"]

sdk = Bytez(api_key)

model = sdk.model("openai/gpt-4.1")

response = model.run([{"role": "user", "content": "HI FRIEND"}])

print(response.output["content"])

