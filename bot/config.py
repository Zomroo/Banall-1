import os

class Config:
    TELEGRAM_TOKEN = os.environ.get('5233700082:AAFFySsOUE5sCMwaInkazxoho0pUR1brJ18')
    TELEGRAM_APP_HASH = os.environ.get('b8105dc4c17419dfd4165ecf1d0bc100')
    TELEGRAM_APP_ID = os.environ.get('15849735')
    
    print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
    print("TELEGRAM_APP_HASH:", TELEGRAM_APP_HASH)
    print("TELEGRAM_APP_ID:", TELEGRAM_APP_ID)
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")

