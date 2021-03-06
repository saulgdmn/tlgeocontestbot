import os

import utility

DEBUG_MODE = True if os.getenv('DEBUG_MODE') == 'true' else False

CONFIG = utility.load_config(os.getenv('CONFIG_PATH'))
LOCALIZATION = utility.load_localization(os.getenv('LOCALIZATION_PATH'))

SERVER_WEBHOOK_IP = os.getenv('SERVER_WEBHOOK_IP')
SERVER_WEBHOOK_PORT = int(os.getenv('SERVER_WEBHOOK_PORT'))

BOT_API_TOKEN = CONFIG.get('BOT_API_TOKEN')
DATABASE_PATH = CONFIG.get('DATABASE_PATH')

HTTP_NODE_URL = CONFIG.get('HTTP_NODE_URL')
CONTRACT_ABI = utility.load_json(os.getenv('CONTRACT_ABI_PATH'))
CONTRACT_ADDRESS = CONFIG.get('CONTRACT_ADDRESS')
PRIVATE_KEY = CONFIG.get('PRIVATE_KEY')

ADMINISTRATOR_IDS = [401042341, 544498153]
DEVELOPER_CHAT_ID = 544498153

CONVERSATION_CHOOSE_LANGUAGE = 1
CONVERSATION_PROVIDE_WALLET = 2
CONVERSATION_TIP_CONFIRM = 3
CONVERSATION_WITHDRAW_CONFIRM = 4

WALLET_PATT = r'^[0-9a-zA-Z]+$'
TIP_PRIVATE_PATT = r'^\/tip\s+\@?(?P<username>[\d\w\s]+)\s+(?P<geocash>[0-9]+)\s+(?P<description>.*)$'
TIP_GROUP_PATT = r'^\/tip\s+(?P<geocash>[0-9]+)\s+(?P<description>.*)$'
