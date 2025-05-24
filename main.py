import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="token.env")
token = os.environ["token"]

