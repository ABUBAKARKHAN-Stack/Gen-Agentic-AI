import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My Name is Abubakar"

tokens = enc.encode(text)

print("Tokens",tokens)

decoded = enc.decode(tokens)
print(decoded)