import os
class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1342512423:AAECV8WwvLxrNIAZgP2ANJ7fSUzY555ubUs"
    DATABASE_URL = "postgres://eronfbflvlwsjs:806fb979f966d7fb4ded82b9753f3dcac29491298c82b4a5a93ef47137c50956@ec2-52-1-95-247.compute-1.amazonaws.com:5432/deae3q32jltnkd"
    APP_ID = "1425367"
    API_HASH = "e8d6126a339ef13fca612c75d2c160f4"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(411872315)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "__ എന്താ ചേട്ടാ ബണ്ടു nte  ഹെല്പ് വേണോ __",
        
        "__ എൻറെ പൊന്നു ചേട്ടാ എനിക്ക് ഒരു പണിയും അറിയില്ല എന്നെ കൊണ്ട് @akhilbaiju  ഇവൻ പണി എടുപ്പിക്കുന്നത് അല്ലെ __",
        
        "__ ചേട്ടന് എന്നെ വേണേൽ ചേട്ടൻ പൈസ കൊടുത്ത  ഇവന്റെ കൈയിൽ  നിന്നും വാങ്ങിക്കോ __",
        
        "**Developed by @akhilbaiju**"
      ]

      START_MSG = "**ഹലോ [{}](tg://user?id={})**\n__എന്താണ്  ഇവിടെ കിടന്നു ഒരു  ചുറ്റി  കറക്കം . \n എന്തേലും ഹെല്പ് വേണേൽ ഇവിടെ Click ചെയ് /help__"
