import os

from dotenv import load_dotenv

if "APP_ENV" not in os.environ:
    load_dotenv()

APP_ENV = os.environ.get("APP_ENV", "development")
IS_DEVELOPMENT = APP_ENV.lower() == "development"

ATLASSIAN_DOMAIN = os.environ.get("ATLASSIAN_DOMAIN")
ATLASSIAN_USERNAME = os.environ.get("ATLASSIAN_USERNAME")
ATLASSIAN_API_TOKEN = os.environ.get("ATLASSIAN_API_TOKEN")

DATABASE_URL = os.environ.get("DATABASE_URL")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
HF_API_TOKEN = os.environ.get("HF_API_TOKEN")

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_EXPIRATION_MINUTES = int(os.environ.get("JWT_EXPIRATION_MINUTES", 30))
