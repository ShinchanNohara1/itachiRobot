# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1670991 # integer value, dont use ""
    API_HASH = "2ff143ba2b9e09a40bf1dc4a99f4d528"
    TOKEN = "1080926584:AAFuAV4izhA6HWHSpjuW2lL0-84lh91aJS4"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1202112402  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Captainlevix"
    SUPPORT_CHAT = 'uchihaclanx'  #Your own group for support, do not add the @
    JOIN_LOGGER = -  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK =  paypal.me/tusharpal4 # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = '3ECNUSP3X6K9V7PJ'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'GNQ6E23C4B0S'  # Get your API key from https://timezonedb.com/api
    WALL_API = '319020ffa5c540d28ddf07061be8112b'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '3b7dfa427e36650dfcc030687d6c5ed04f895bb00c16313b9a451e9ce61635132d95401f3c8f7a119b0fe28300ec8e88084348dee34924c41080486875b8284e'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
