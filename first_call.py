import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = {
    "role": "system",
    "content": "You are a helpful assistant."
}

user_input = input("Enter your prompt: ")

user_prompt = {
    "role": "user",
    "content": user_input
}

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, user_prompt]
)

assistant_reply = response.choices[0].message.content
print("\nAssistant's Reply:\n", assistant_reply)

usage = response.usage
print("\nToken Usage:")
print(f"Prompt Tokens: {usage.prompt_tokens}")
print(f"Completion Tokens: {usage.completion_tokens}")
print(f"Total Tokens: {usage.total_tokens}")
