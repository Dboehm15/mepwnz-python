from dotenv import load_dotenv
import os

load_dotenv()
HOST = "https://us.api.blizzard.com/"
ACCESS_TOKEN = os.getenv('access_token')
