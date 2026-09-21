from ollama import chat

response = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explain an AI agent in simple terms."
        }
    ]
)

print(response.message.content)