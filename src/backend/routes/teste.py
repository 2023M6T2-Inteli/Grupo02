from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("url")
key = os.getenv("api_key")


print("url",url)