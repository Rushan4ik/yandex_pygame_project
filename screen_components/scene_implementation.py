from screen_components import Scene
from widgets import Button, Label, Slider


class MainMenuScene(Scene):
    def __init__(self):
        buttons = [Button((200, 10), (100, 60), "Start", [Button.Handler(lambda: print("Start"))])]
        sliders = [Slider((50, 200), (300, 20), (10, 300), 40, [Slider.Handler(lambda x: print("Value:", x))])]
        labels = []
        super().__init__(buttons, sliders, labels)
