from mistralai.client import MistralClient
from config.config import Config

class CodestralIntegration:
    def __init__(self):
        self.api_key = Config.API_KEY
        self.client = MistralClient(api_key=self.api_key)
        self.model = "codestral-latest"

    def generate_code(self, prompt, suffix="", stop=None):
        response = self.client.completion(
            model=self.model,
            prompt=prompt,
            suffix=suffix,
            stop=stop
        )
        return response.choices[0].message.content

    def review_code(self, prompt):
        response = self.client.completion(
            model=self.model,
            prompt=prompt
        )
        return response.choices[0].message.content
