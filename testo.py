import pytz
import datetime

class Buganda(pytz.timezone("Africa/Kampala")):
    zone = "Africa/Buganda"

    def tzname(self):
        return "BUG"
