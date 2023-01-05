from screen_components import Scene
from screen_components.scene_implementation import MainMenuScene


class SceneManager:
    def __init__(self):
        self.current_scene = MainMenuScene()

    def get_current_scene(self) -> Scene:
        return self.current_scene
