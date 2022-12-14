import pygame
from pygame.sprite import Sprite, AbstractGroup, collide_mask
from pygame import Surface
from pygame.mask import from_surface
from game_components.entity import Entity
WALL_COLOR = pygame.Color(0, 0, 0)


class Wall(Sprite):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = Surface(size)
        self.image.fill(WALL_COLOR)
        self.rect, self.mask = self.image.get_rect().move(*position), from_surface(self.image)

    def update(self, *args, **kwargs) -> None:
        if 'entity' in kwargs:
            self.handle_entity(kwargs['entity'])

    def handle_entity(self, entity: Entity) -> None:
        if not collide_mask(self, entity):
            return
        intersection = entity.rect.clip(self.rect)
        if intersection.w >= intersection.h:
            # handle as floor
            self._handle_horizontal(entity)
        else:
            # handle as wall
            self._handle_vertical(entity)

    def _handle_vertical(self, entity) -> None:
        x, w = self.rect.x, self.rect.w
        x1, x2 = entity.rect.x, entity.rect.x + entity.rect.w
        if x1 < x < x2:
            entity.velocity.x = 0
            entity.set_position(x + entity.rect.w, entity.position.y)
        if x1 < x + w < x2:
            entity.velocity.x = 0
            entity.set_position(x + w, entity.position.y)

    def _handle_horizontal(self, entity) -> None:
        y, h = self.rect.y, self.rect.h
        y1, y2 = entity.rect.y, entity.rect.y + entity.rect.h
        if y1 < y < y2:
            entity.on_ground = True
            entity.velocity.y = 0
            entity.set_position(entity.position.x, y - entity.rect.h + 1)
        if y1 < y + h < y2:
            entity.velocity.y = 0
            entity.set_position(entity.position.x, y + h)


# ||
class VerticalWall(Wall):
    def handle_entity(self, entity: Entity) -> None:
        if not collide_mask(self, entity):
            return
        x, w = self.rect.x, self.rect.w
        x1, x2 = entity.rect.x, entity.rect.x + entity.rect.w
        if x1 < x < x2:
            entity.velocity.x = 0
            entity.set_position(x + entity.rect.w, entity.position.y)
        if x1 < x + w < x2:
            entity.velocity.x = 0
            entity.set_position(x + w, entity.position.y)


# =
class HorizontalWall(Wall):
    def handle_entity(self, entity: Entity) -> None:
        if not collide_mask(self, entity):
            return
        y, h = self.rect.y, self.rect.h
        y1, y2 = entity.rect.y, entity.rect.y + entity.rect.h
        if y1 < y < y2:
            entity.on_ground = True
            entity.velocity.y = 0
            entity.set_position(entity.position.x, y - entity.rect.h + 1)
        if y1 < y + h < y2:
            entity.velocity.y = 0
            entity.set_position(entity.position.x, y + h)
