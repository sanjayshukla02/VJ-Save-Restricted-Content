import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26233428"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be1d40c1cc17e8d6fb19edcc835a4866")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sanjayshukla02261:Q73nTvfFc1GXe4FB@cluster0.tjka7x1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
