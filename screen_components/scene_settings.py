import configs
from screen_components import Scene
from widgets import Button, Label, Slider


def set_max_vertical_speed(value):
    configs.MAX_VERTICAL_SPEED = value


def set_graviti_acceleration(value):
    configs.GRAVITY_ACCELERATION = value


def set_animation_speed(value):
    configs.PLAYER_ANIMATION_SPEED = value


def set_player_speed(value):
    configs.PLAYER_SPEED = value


def set_jump_force(value):
    configs.PLAYER_JUMP_FORCE = value


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
            Slider((250, 90), (200, 30), (40, 300), configs.MAX_VERTICAL_SPEED,
                   [Slider.Handler(set_max_vertical_speed)]),
            Slider((250, 130), (200, 30), (10, 50), configs.GRAVITY_ACCELERATION,
                   [Slider.Handler(set_graviti_acceleration)]),
            Slider((250, 170), (200, 30), (0.1, 2), configs.PLAYER_ANIMATION_SPEED,
                   [Slider.Handler(set_animation_speed)]),
            Slider((250, 210), (200, 30), (30, 100), configs.PLAYER_SPEED,
                   [Slider.Handler(set_player_speed)]),
            Slider((250, 250), (200, 30), (20, 100), configs.PLAYER_JUMP_FORCE,
                   [Slider.Handler(set_jump_force)])
        ]
        super().__init__(buttons, sliders, labels)

    def __set_main_menu(self):
        self.scene_manager.set_main_menu_scene()
