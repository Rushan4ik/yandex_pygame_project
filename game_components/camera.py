from game_components import Entity, Wall


class Camera:
    def __init__(self, window_size: tuple[int, int]):
        self.dx = self.dy = 0
        self.width, self.height = window_size

    def update(self, entity: Entity) -> None:
        self.dx = -(entity.rect.x + entity.rect.w // 2 - self.width // 2)
        self.dy = -(entity.rect.y + entity.rect.h // 2 - self.height // 2)

    def apply_entity(self, entity: Entity) -> None:
        x, y = entity.position.x, entity.position.y
        entity.set_position(x + self.dx, y + self.dy)

    def apply_wall(self, wall: Wall) -> None:
        wall.rect.x += self.dx
        wall.rect.y += self.dy
