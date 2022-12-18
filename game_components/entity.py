from pygame.sprite import Sprite, AbstractGroup
from math_components import Vector


class Entity(Sprite):
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
