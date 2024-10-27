import requests

from dotenv import load_dotenv
import os

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
        {"role": "user", "content": "生成AIは、どんな発展をしますか？"}
    ],
    "max_tokens": 100

}

res = requests.post(url, headers=headers, json=data)

result = res.json()
print(result)

print(result["choices"][0]["message"]["content"])

