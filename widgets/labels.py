from pygame import Color, Surface
from pygame.font import Font
from pygame.sprite import Sprite, AbstractGroup


class Label(Sprite):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], text: str,
                 background_color: Color = Color(255, 204, 0), font_color: Color = Color(0, 0, 0), font_size: int = 12,
                 font: str = 'Arial', *groups: AbstractGroup):
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

