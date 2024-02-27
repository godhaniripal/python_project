import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
print(f'the secret key is {SECRET_KEY}')
