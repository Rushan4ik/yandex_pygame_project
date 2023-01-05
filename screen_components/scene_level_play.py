from game_components import Level
from screen_components import Scene
from widgets import Button


def load_level(level_number: int) -> Level | None:
    return Level((1, 1), [], [], (1, 1))


class LevelScene(Scene):
    def __init__(self, scene_manager, level_number: int):
        self.scene_manager = scene_manager
        self.level = load_level(level_number)
        buttons = [Button((20, 20), (20, 20), "<-", [Button.Handler(self.__set_main_menu)]),
                   Button((50, 20), (20, 20), "()", [Button.Handler(self.level.restart)])]
        super().__init__(buttons, [], [], self.level)

    def __set_main_menu(self):
        self.scene_manager.set_main_menu_scene()

    def update(self, duration):
        super().update(duration)
        if self.level.player.live_count == 0:
            self.__set_main_menu()

