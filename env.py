import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27639102").strip()
API_HASH = os.getenv("API_HASH", "35142c1407be6264e68fb6bec5dcabd9").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6191852838:AAG6RpgZO0EV_zrivbUO9j31h3N4_bZRTgg").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Forward123:Forward123@cluster0.4d1ljfv.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = os.getenv("MUST_JOIN", "https://t.me/VJ_Bots")

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
