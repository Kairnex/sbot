from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "24509589"))
API_HASH = getenv("API_HASH", "717cf21d94c4934bcbe1eaa1ad86ae75")

BOT_TOKEN = getenv("BOT_TOKEN", "7493562717:AAH9DGdNRk5g_kCQ6hxLR39szY-WacI8At0")
OWNER_ID = int(getenv("OWNER_ID", "7225660023"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
MUST_JOIN = getenv("MUST_JOIN", "sacnetwork")
DAXX_API = getenv("DAXX_API", "")
