from lib.game import Game

from .api.api import OLDTVAPI

from lib.utilities import Singleton


class SerpentOLDTVGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "V"

        kwargs["executable_path"] = "oldtv"

        super().__init__(**kwargs)

        self.api_class = OLDTVAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "MAIN_MENU": (0,0,0)
        }

        return regions
