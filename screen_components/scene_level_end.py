from screen_components import Scene
from widgets import Label


class LevelEndScene(Scene):
    def __init__(self, scene_manager, result: float):
        self.scene_manager = scene_manager
        super().__init__([], [], [Label((100, 100), (200, 100), f'Your result:\n{result} sec')])

    def handle_press(self, event):
        self.scene_manager.set_main_menu_scene()
