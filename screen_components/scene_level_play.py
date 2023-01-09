from game_components import Level, Wall, Finish, Fire
from screen_components import Scene
from widgets import Button
import sqlite3


def load_level(window_size: tuple[int, int], level_number: int,
               generate: bool = False) -> Level | None:
    if generate:
        return Level(window_size,
                     [Wall((0, 0), (60, 200)),
                      Wall((0, 300), (100, 30))],  # WALLS
                     [Fire((20, 280), (20, 20))],  # SPIKES
                     [],  # ENTITIES
                     (100, 1),
                     [Finish((200, 300), (50, 50))])

    with sqlite3.connect('database.sqlite') as connection:
        pass  # TODO: load from DB


class LevelScene(Scene):
    def __init__(self, scene_manager, level_number: int):
        self.scene_manager = scene_manager
        # TODO: CORRECT THAT WHEN YOU SET UP DB
        self.level = load_level(scene_manager.window_size, level_number, True)
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
