# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23673651"))
API_HASH = getenv("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b")
BOT_TOKEN = getenv("BOT_TOKEN", "8307502375:AAH0_nZ784i-0Hdg4d75TlpIveBMbV7ynqE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6677821706").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://King0077637373:945544Mk@#@cluster0.vjydpkn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003047586469")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002755790239"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
