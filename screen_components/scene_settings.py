import configs
from screen_components import Scene
from widgets import Button, Label, Slider
from json import load, dump


class SettingsScene(Scene):
    PARAM_NAMES = ["MAX VERTICAL SPEED", "GRAVITY", "ANIMATION SPEED",
                   "PLAYER SPEED", "PLAYER JUMP FORCE"]

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.json_value = load(open('configs.json'))
        buttons = [Button((20, 20), (50, 50), "BACK", [Button.Handler(self.__set_main_menu)])]
        labels = []
        for i, text in enumerate(SettingsScene.PARAM_NAMES):
            labels.append(Label((90, 90 + 40 * i), (140, 30), text, font_size=10))
        sliders = [
            Slider((250, 90), (200, 30), (40, 300), self.json_value['MAX_VERTICAL_SPEED'],
                   [Slider.Handler(lambda value: self.set_max_vertical_speed(value))]),
            Slider((250, 130), (200, 30), (10, 50), self.json_value['GRAVITY_ACCELERATION'],
                   [Slider.Handler(lambda value: self.set_graviti_acceleration(value))]),
            Slider((250, 170), (200, 30), (0.1, 2), self.json_value['PLAYER_ANIMATION_SPEED'],
                   [Slider.Handler(lambda value: self.set_animation_speed(value))]),
            Slider((250, 210), (200, 30), (30, 100), self.json_value['PLAYER_SPEED'],
                   [Slider.Handler(lambda value: self.set_player_speed(value))]),
            Slider((250, 250), (200, 30), (20, 100), self.json_value['PLAYER_JUMP_FORCE'],
                   [Slider.Handler(lambda value: self.set_jump_force(value))])
        ]
        super().__init__(buttons, sliders, labels)

    def set_max_vertical_speed(self, value):
        self.json_value['MAX_VERTICAL_SPEED'] = value

    def set_graviti_acceleration(self, value):
        self.json_value['GRAVITY_ACCELERATION'] = value

    def set_animation_speed(self, value):
        self.json_value['PLAYER_ANIMATION_SPEED'] = value

    def set_player_speed(self, value):
        self.json_value['PLAYER_SPEED'] = value

    def set_jump_force(self, value):
        self.json_value['PLAYER_JUMP_FORCE'] = value

    def __set_main_menu(self):
        self.save()
        self.scene_manager.set_main_menu_scene()

    def save(self):
        dump(self.json_value, open('configs.json', 'w'))
