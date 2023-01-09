from game_components import Level
from screen_components import Scene
from widgets import Button
from game_components import VerticalWall, HorizontalWall, Spike


def load_level(window_size: tuple[int, int], level_number: int) -> Level | None:
    return Level(window_size,
                 [VerticalWall((0, 0), (60, 500)),
                  VerticalWall((700, 0), (30, 500)),
                  HorizontalWall((500, 60), (730, 40))],  # WALLS
                 [],  # SPIKES
                 [],  # ENTITIES
                 (1, 1))


class LevelScene(Scene):
    def __init__(self, scene_manager, level_number: int):
        self.scene_manager = scene_manager
        self.level = load_level(scene_manager.window_size, level_number)
        buttons = [Button((20, 20), (20, 20), "<-", [Button.Handler(self.__set_main_menu)]),
                   Button((50, 20), (20, 20), "()", [Button.Handler(self.level.restart)])]
        super().__init__(buttons, [], [], self.level)

    def __set_main_menu(self):
        self.scene_manager.set_main_menu_scene()

    def update(self, duration):
        super().update(duration)
        if self.level.player.live_count == 0:
            self.__set_main_menu()
        if self.level.running is False:
            self.scene_manager.set_level_end_scene(self.level.get_result())
