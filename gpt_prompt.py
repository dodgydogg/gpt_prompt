import os
import requests
import json
import pandas as pd

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

def prompt(verdict_text):
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    body = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "幫我把以下文字翻譯成繁體中文"},
            {"role": "user", "content": verdict_text}
        ],
        "max_tokens": 2048
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(body))
    parsed_content = response.json()
    
    counsel_name_gpt = parsed_content["choices"][0]["message"]["content"]
    return counsel_name_gpt




