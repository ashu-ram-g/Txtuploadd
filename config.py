import os

API_ID = API_ID = 18116881

API_HASH = os.environ.get("API_HASH", "cca3bacf40fb3ebcb4f075b2e46ff1bd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7958229600:AAHqpzrkOdzCNn-0QF5JOsi6bLvuxn9ETBM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1445673621))

LOG = , -1002020978757

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1445673621").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


