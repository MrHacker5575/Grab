class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5129320633"
    sudo_users = "5129320633"
    GROUP_ID = "-1002033678903"
    TOKEN = "6953609281:AAFPPU7z0AbVmdRfdrV5OLJbQTOocnmnrTg"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = ""
    UPDATE_CHAT = ""
    BOT_USERNAME = "spamsabot"
    CHARA_CHANNEL_ID = "-1002033678903"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
