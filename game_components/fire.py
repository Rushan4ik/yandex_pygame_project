import pygame.draw
from pygame import Surface, Color
from pygame.mask import from_surface
from pygame.sprite import Sprite, AbstractGroup, collide_mask
from game_components import Player

FIRE_COLOR = Color(255, 0, 0)


class Fire(Sprite):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = Surface(size)
        w, h = size
        self.image.fill(FIRE_COLOR)
        self.rect, self.mask = self.image.get_rect().move(*position), from_surface(self.image)

    def handle_entity(self, player: Player):
        return bool(collide_mask(player, self))

