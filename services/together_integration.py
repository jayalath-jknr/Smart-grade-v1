import os
import requests
from dotenv import load_dotenv

load_dotenv()

class TogetherLlamaIntegration:
    def __init__(self):
        self.api_key = os.getenv('TOGETHER_API_KEY')
        self.base_url = "https://api.together.xyz/v1/chat/completions"

    def generate_code(self, prompt):
        response = requests.post(
            self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "code-llama",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def review_code(self, code_snippet):
        prompt = f"Review the following C++ code and provide feedback:\n\n{code_snippet}"
        response = requests.post(
            self.base_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "code-llama",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
