import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "15377279").strip()
API_HASH = os.getenv("API_HASH", "9b4f9729873e22a7a30a121edc6c1f70").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6339227402:AAFXFuSFMX-m-StrFer4v_B1fWe18m0Z0iI").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://alrufaaey:engmomo-1@cluster0.9zpctum.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/BBeBB")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
