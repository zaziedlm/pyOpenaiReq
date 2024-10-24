from openai import OpenAI
from dotenv import load_dotenv
import os

# .env ファイルから環境変数を読み込む
load_dotenv()

# 環境変数を取得
api_key = os.getenv('OPENAI_API_KEY')
llm_url = os.getenv('LLM_BASE_URL')
llm_model = os.getenv('LLM_MODEL')

# OpenAI クライアントを初期化
openai_client = OpenAI(
    api_key=api_key,
    base_url=llm_url,
)

completion = openai_client.chat.completions.create(
    model=llm_model,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "日本で一番高い山はなんでしょうか？"
        }
    ]
)

print(completion.choices[0].message)