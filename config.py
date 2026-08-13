import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.guvi.in"
LOGIN_URL = "https://www.guvi.in/sign-in/"
REGISTER_URL = "https://www.guvi.in/register/"

VALID_EMAIL = os.getenv("GUVI_EMAIL")
VALID_PASSWORD = os.getenv("GUVI_PASSWORD")

INVALID_EMAIL = "invaliduser123@gmail.com"
INVALID_PASSWORD = "WrongPassword@123"