from serpent.game_api import GameAPI


class OLDTVAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)


    class MainMenu:

        @classmethod
        def click_options(cls):
            OLDTVAPI.instance.input_controller.click_screen_region(
                screen_region="MAIN_MENU_OPTIONS"
            )
