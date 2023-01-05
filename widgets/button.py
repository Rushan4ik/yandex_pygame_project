import pygame
from pygame import Surface
from pygame.sprite import Sprite, AbstractGroup
from pygame.color import Color
from pygame.font import Font
from typing import Callable


class Button(Sprite):
    class Handler:
        def __init__(self, callback: Callable[[], None]):
            self.callback = callback

        def apply(self):
            self.callback()

    def __init__(self, position: tuple[int, int],
                 size: tuple[int, int], text: str,
                 handlers: list[Handler] | None = None,
                 background_color: Color = Color(255, 204, 0),
                 font_color: Color = Color(0, 0, 0), font_size: int = 12,
                 font: str = 'Arial',
                 *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = Surface(size)
        self.image.fill(background_color)
        self.font = Font(font, font_size)
        self.text = self.font.render(text, True, font_color, background_color)
        self.rect = self.image.get_rect().move(*position)
        shift_x, shift_y = [(image_size - text_size) // 2
                            for text_size, image_size in zip(self.text.get_rect(),
                                                             self.image.get_rect())]
        self.image.blit(self.text, (shift_x, shift_y))
        if handlers is None:
            handlers = []
        self.handlers = handlers

    def update(self, event=None) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_press((event.x, event.y))

    def handle_press(self, coords):
        if self.rect.collidepoint(*coords):
            self.on_click()

    def on_click(self):
        for handler in self.handlers:
            handler.apply()

    def add_handler(self, handler: Handler) -> None:
        self.handlers.append(handler)
