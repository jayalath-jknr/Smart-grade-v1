from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_KEY = os.getenv('MISTRAL_API_KEY')
