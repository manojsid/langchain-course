import requests
import os
import json

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
}

response = requests.get(url, headers=headers)

if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Status: {response.status_code}")
    print(response.text)