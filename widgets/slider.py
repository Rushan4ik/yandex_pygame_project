from typing import Callable

import pygame.draw
from pygame import Color, Surface
from pygame.sprite import Sprite, AbstractGroup


class Slider(Sprite):
    class Handler:
        def __init__(self, callback: Callable[[int | float], None]):
            self.callback = callback

        def apply(self, value: int | float):
            self.callback(value)

    def __init__(self, position: tuple[int, int],
                 size: tuple[int, int], text: str,
                 min_max_value, value,
                 handlers: list[Handler] | None = None,
                 background_color: Color = Color(255, 204, 0),
                 *groups: AbstractGroup):
        self.image = Surface(size)
        self.image.fill(background_color)
        self.background_color = background_color
        self.rect = self.image.get_rect().move(*position)
        self.min, self.max = min_max_value
        self.value = value
        self.value_x = self.value / (self.max - self.min) * self.rect.w + self.rect.x
        if handlers is None:
            handlers = []
        self.handlers = handlers
        super().__init__(*groups)

    def handle_press(self, coords):
        if self.rect.collidepoint(*coords):
            self.value_x = coords[0]
            self.value = (self.value_x - self.rect.x) / self.rect.w * (self.max - self.min) + self.min
            self.on_click()

    def on_click(self):
        self.repaint()
        for handler in self.handlers:
            handler.apply(self.value)

    def add_handler(self, handler: Handler) -> None:
        self.handlers.append(handler)

    def repaint(self):
        self.image.fill(self.background_color)
        pygame.draw.line(self.image, Color(200, 200, 200), (0, self.rect.h // 2), (self.rect.w, self.rect.h // 2), 5)
        pygame.draw.circle(self.image, Color(100, 100, 100), (self.value_x, 0), 20)
