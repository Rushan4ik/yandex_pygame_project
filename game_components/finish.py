from pygame.mask import from_surface
from pygame.sprite import Sprite, AbstractGroup, collide_mask
from pygame import Color, Surface

from game_components import Player

FINISH_COLOR = Color(0, 255, 0)


class Finish(Sprite):
    def __init__(self, position: tuple[int, int],
                 size: tuple[int, int], *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = Surface(size)
        self.image.fill(FINISH_COLOR)
        self.rect, self.mask = self.image.get_rect().move(*position), from_surface(self.image)

    def handle_entity(self, player: Player):
        return bool(collide_mask(self, player))
