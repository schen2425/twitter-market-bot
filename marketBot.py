from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('test')
print(API_KEY)