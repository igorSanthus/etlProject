import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

api_key = os.getenv("API_KEY")


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {    "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Quantos juizes corruptos existem no Brasil?"}]}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json()['choices'][0]['message']['content']) 
