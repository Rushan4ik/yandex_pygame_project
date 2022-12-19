from pygame.sprite import Sprite, AbstractGroup


class Wall(Sprite):
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
