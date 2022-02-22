import os

class Config:
    BOT_TOKEN = os.environ.get("5148891104:AAGVQQjlidRf57Rr1khrRnB2_lPXzWs3cUY","")
    HEROKU_API_KEY = os.environ.get("d502dd68-3121-40a1-b5e2-0b5d28e56efa","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("1380112160").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("ets-m1-161","")
