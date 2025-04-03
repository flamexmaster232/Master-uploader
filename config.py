import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8126174019:AAHnlSyI4oA3k3qKTnTwRGU2q3ohECBOmUs")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "23612641"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "f7ef90c733241bdc2977e3fcc53df5b7")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7769588492").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
