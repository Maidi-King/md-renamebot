import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = int(os.environ.get("API_ID", "25065882"))
    API_HASH = os.environ.get("API_HASH" "7711af532d45686e38c6b360161e2483")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6953329998:AAFQmTdAjYWpF0aC63iKZBZqnJ6QTrB_3XI")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6302537270"))
    AUTH_CHANNEL = os.environ.get("AUTH_CHANNEL", "-1002098883316")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://myd:1mSbGWcHHGpFhcwg@cluster0.pl3b8ro.mongodb.net/?retryWrites=true&w=majority")
