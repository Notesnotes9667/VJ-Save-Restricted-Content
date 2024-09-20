import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25369773"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3063f34c849ee3561050703e936725a3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://notesnotes9667:O7sE9e5msvN0ar0e@cluster0.wbdr7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
