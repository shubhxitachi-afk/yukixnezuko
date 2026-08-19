#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
# Get it from my.telegram.org
API_ID = 34829388
API_HASH = "30df7fd725bd39aa2e3b7a55b15a182b"

## Get it from @Botfather in Telegram.
BOT_TOKEN = "8954458459:AAHRTJucDx31wUKbCQhF0ICzJ4pUtN5_VuE"

# SUDO USERS
SUDO_USER = [8888788314]
# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("-1004405902404"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello!",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("mongodb+srv://shubhxitachi_db_user:3r1jKiHGmAyd93wy@nezukonbot.wkzudm6.mongodb.net/?retryWrites=true&w=majority", None)
