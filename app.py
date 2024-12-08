import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
url = os.getenv("LLM_BASE_URL") + "chat/completions"
model = os.getenv("LLM_MODEL")


# HTTP headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# The request payload chat jsondata
data = {
    "model": model,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "AIの可能性について教えて"}
    ],
    "max_tokens": 1024
}

# Send request
res = requests.post(url, headers=headers, json=data)

# Print response
result = res.json()
print(result)

# Access the content of the assistant's message
if "choices" in result:
    print(result["choices"][0]["message"]["content"])
else:
    print("Error:", result.get("error", {}).get("message", "Unknown error"))







