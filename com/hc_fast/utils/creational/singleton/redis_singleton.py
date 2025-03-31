import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로딩

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
