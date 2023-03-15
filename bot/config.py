import os

class Config:
    TELEGRAM_TOKEN=os.environ['5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8']
    TELEGRAM_APP_HASH=os.environ['b8105dc4c17419dfd4165ecf1d0bc100']
    TELEGRAM_APP_ID=int(os.environ['15849735'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
