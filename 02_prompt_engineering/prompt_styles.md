# Prompt Styles

## 1. Alpaca Prompt

### Format:
```
### Instructions:

<SYSTEM_PROMPT>

### Input:
<USER_QUERY>

### Response:
```
### Examples

Q1: Write an Alpaca prompt to add two numbers  
A:
```
### Instructions:
Add the two numbers provided in the input and return the result.

### Input:
6, 7

### Response:
```

Q2: Convert this into an Alpaca prompt
{
  "role": "user",
  "content": "Hey"
}

A:
```
### Instructions:
Respond to the given input.

### Input:
Hey

### Response:
```

## 2. CHAT/ML Prompt

### Format:
```py

{
    "role": "system" | "user" | "assistant",
    "content": "string"
}
```

### Example:
```py
{
  "role": "user",
  "content": "Write a Python function to add two numbers."
}
```


## 3. INST Prompt

### Format:

```
[INST] <User-Query> [/INST]
```

### Example:

```
[INST] Write a TypeScript function to add n numbers [/INST]
```
