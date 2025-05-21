import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "29847446"))
    API_HASH = os.environ.get("API_HASH", "4700afc0a414f298c3c70657e5f11cc8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7861909705:AAEITArdXG4xW_BE_Qb5yl0wL8Yh_iUk5g8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "raazh_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
