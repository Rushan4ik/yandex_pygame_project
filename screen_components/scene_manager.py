from screen_components import Scene
from screen_components.scene_level_choice import LevelChoiceScene
from screen_components.scene_level_end import LevelEndScene
from screen_components.scene_level_play import LevelScene
from screen_components.scene_main import MainMenuScene
from screen_components.scene_settings import SettingsScene


class SceneManager:
    def __init__(self):
        self.current_scene = None
        self.window_size = 1, 1

    def get_current_scene(self) -> Scene:
        return self.current_scene

    def set_main_menu_scene(self) -> None:
        self.current_scene = MainMenuScene(self)

    def set_settings_scene(self) -> None:
        self.current_scene = SettingsScene(self)

    def set_level_choice_scene(self) -> None:
        self.current_scene = LevelChoiceScene(self)

    def set_level_scene(self, level_number: int) -> None:
        self.current_scene = LevelScene(self, level_number)

    def set_level_end_scene(self, result: float) -> None:
        self.current_scene = LevelEndScene(self, result)

