from configs import LEVEL_COUNT
from screen_components import Scene
from widgets import Button


class LevelChoiceScene(Scene):
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        buttons = [Button((20, 20), (50, 50), "BACK", [Button.Handler(self.__set_main_menu)])]
        for i in range(LEVEL_COUNT):
            button = Button((80 + i * 120, 100), (100, 100), str(i + 1), [Button.Handler(self.__create_level_handler(i))])
            buttons.append(button)
        super().__init__(buttons, [], [])

    def __set_main_menu(self):
        self.scene_manager.set_main_menu_scene()

    def __create_level_handler(self, num: int):
        return lambda: self.scene_manager.set_level_scene(num + 1)
