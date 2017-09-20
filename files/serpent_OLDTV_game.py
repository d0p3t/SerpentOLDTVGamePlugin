from serpent.game import Game

from .api.api import OLDTVAPI

from serpent.utilities import Singleton


class SerpentOLDTVGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "V"

        kwargs["app_id"] = "643270"
        kwargs["app_args"] = None


        super().__init__(**kwargs)

        self.api_class = OLDTVAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            # "SCREEN_REGION": (y1, x1, y2, x2)
            "MAIN_MENU_OPTIONS": (462, 138, 518, 194),
            "MAIN_MENU_STATS": (462, 828, 518, 884),
            "MAIN_MENU_MAIL": (71, 822, 125, 896),
            "MAIN_MENU_THUNDER": (66, 136, 129, 199)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
