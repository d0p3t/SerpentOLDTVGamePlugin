from lib.game_api import GameAPI


class OLDTVAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class MainMenu:

        @classmethod
        def my_namespaced_api_function(cls):
            api = OLDTVAPI.instance
