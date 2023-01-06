import configs
from screen_components import Scene
from widgets import Button, Label, Slider
from game_components.utils import set_configs_param, get_configs_param


class SettingsScene(Scene):
    PARAM_NAMES = ["MAX VERTICAL SPEED", "GRAVITY", "ANIMATION SPEED",
                   "PLAYER SPEED", "PLAYER JUMP FORCE"]

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        buttons = [Button((20, 20), (50, 50), "BACK", [Button.Handler(self.__set_main_menu)])]
        labels = []
        for i, text in enumerate(SettingsScene.PARAM_NAMES):
            labels.append(Label((90, 90 + 40 * i), (140, 30), text, font_size=10))
        sliders = [
            Slider((250, 90), (200, 30), (40, 300), get_configs_param('MAX_VERTICAL_SPEED'),
                   [Slider.Handler(lambda value: set_configs_param('MAX_VERTICAL_SPEED', value))]),
            Slider((250, 130), (200, 30), (10, 50), get_configs_param('GRAVITY_ACCELERATION'),
                   [Slider.Handler(lambda value: set_configs_param('GRAVITY_ACCELERATION', value))]),
            Slider((250, 170), (200, 30), (0.1, 2), get_configs_param('PLAYER_ANIMATION_SPEED'),
                   [Slider.Handler(lambda value: set_configs_param('PLAYER_ANIMATION_SPEED', value))]),
            Slider((250, 210), (200, 30), (30, 100), get_configs_param('PLAYER_SPEED'),
                   [Slider.Handler(lambda value: set_configs_param('PLAYER_SPEED', value))]),
            Slider((250, 250), (200, 30), (20, 100), get_configs_param('PLAYER_JUMP_FORCE'),
                   [Slider.Handler(lambda value: set_configs_param('PLAYER_JUMP_FORCE', value))])
        ]
        super().__init__(buttons, sliders, labels)

    def __set_main_menu(self):
        self.scene_manager.set_main_menu_scene()

