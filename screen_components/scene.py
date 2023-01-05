import pygame

from game_components import Level
from widgets import Slider, Button, Label
from pygame.sprite import Group


class Scene:
    def __init__(self, buttons: list[Button],
                 sliders: list[Slider], labels: list[Label], level: Level | None = None):
        self.buttons = Group(buttons)
        self.sliders = Group(sliders)
        self.labels = Group(labels)
        self.level = level

    def draw(self, screen):
        if self.level is not None:
            self.level.draw(screen)
        self.labels.draw(screen)
        self.sliders.draw(screen)
        self.buttons.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_press(event)
        if self.level is not None:
            self.level.handle_event(event)

    def handle_press(self, event):
        self.buttons.update(event=event)
        self.sliders.update(event=event)

    def update(self, duration):
        if self.level is not None:
            self.level.update(duration)
