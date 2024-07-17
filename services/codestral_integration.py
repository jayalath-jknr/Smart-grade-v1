import subprocess
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

    def review_code(self, code_snippet):
        response = self.client.completion(
            model=self.model,
            prompt=code_snippet
        )
        return response.choices[0].message.content

    def execute_code(self, code_snippet):
        try:
            with open("temp_code.cpp", "w") as code_file:
                code_file.write(code_snippet)
            compile_result = subprocess.run(["g++", "temp_code.cpp", "-o", "temp_code"], capture_output=True, text=True)
            if compile_result.returncode != 0:
                return compile_result.stderr, False
            run_result = subprocess.run(["./temp_code"], capture_output=True, text=True)
            return run_result.stdout, True
        except Exception as e:
            return str(e), False

    def correct_code(self, error_message):
        response = self.client.completion(
            model=self.model,
            prompt=f"Correct the following C++ code error: {error_message}"
        )
        return response.choices[0].message.content
