from widgets import Slider, Button
from pygame.sprite import Group


class Scene:
    def __init__(self, buttons: list[Button], sliders: list[Slider], level=None):
        self.buttons = Group(buttons)
        self.sliders = Group(sliders)

    def draw(self, screen):
        pass


