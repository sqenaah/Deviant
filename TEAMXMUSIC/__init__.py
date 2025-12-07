from TEAMXMUSIC.core.bot import JARVIS
from TEAMXMUSIC.core.dir import dirr
from TEAMXMUSIC.core.git import git
from TEAMXMUSIC.core.userbot import Userbot
from TEAMXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = JARVIS()
# ❌ DISABLED: Don't create userbot during module import to prevent session validation
userbot = None


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
