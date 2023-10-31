from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID", "6495765183"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c618b2f8dbfff3b9e47b9.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/62f7f88aaa51a37dbde8c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CYBERczy")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ABT_KINGxYT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6495765183").split()))


FAILED = "https://telegra.ph/file/538dfef99c9212e6c934a.jpg"
