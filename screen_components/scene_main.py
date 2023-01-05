from screen_components import Scene
from widgets import Button


class MainMenuScene(Scene):

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        buttons = [Button((150, 100), (200, 60), "LEVELS", [Button.Handler(self.__set_level_choice)]),
                   Button((150, 170), (200, 60), "SETTINGS", [Button.Handler(self.__set_settings)])]
        super().__init__(buttons, [], [])

    def __set_level_choice(self):
        self.scene_manager.set_level_choice_scene()

    def __set_settings(self):
        self.scene_manager.set_settings_scene()
