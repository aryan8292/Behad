from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = environ.get("API_ID", "24519928")
API_HASH = environ.get("API_HASH", "52ffd10fc020f69854d3df7299a70577")
BOT_TOKEN = environ["BOT_TOKEN"]
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002022608853"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5079629749').split()]
TARGET_DB = int(environ.get("TARGET_DB", 0))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://t.me/+KEFFPpO-q90wNDNl")
