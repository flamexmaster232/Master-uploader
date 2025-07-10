import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8170296110:AAH-K-oFjHz2TU1bH14wpi2F-0o5BuRgj4k")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "26548330"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "244c3afd019c7b0cd1a8184cd2be2495")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6890753169").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
