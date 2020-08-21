import os

import utility

DEBUG_MODE = True if os.getenv('DEBUG_MODE') == 'true' else False

CONFIG = utility.load_config(os.getenv('CONFIG_PATH'))
LOCALIZATION = utility.load_localization(os.getenv('LOCALIZATION_PATH'))

BOT_API_TOKEN = CONFIG.get('BOT_API_TOKEN')
DATABASE_PATH = CONFIG.get('DATABASE_PATH')

ADMINISTRATOR_IDS = [401042341, 544498153]
DEVELOPER_CHAT_ID = 544498153

CONVERSATION_CHOOSE_LANGUAGE = 1
CONVERSATION_PROVIDE_WALLET = 2
CONVERSATION_TIP_CONFIRM = 3

WALLET_PATT = r'^[0-9a-z]+$'
TIP_PATT = r'^\/tip\s+\@?(?P<username>[\d\w\s]+)\s+(?P<geocash>[0-9]+)\s+(?P<description>.*)$'
