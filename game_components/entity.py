from pygame.sprite import Sprite, AbstractGroup
from utils import load_image
from math_components import Vector
from pygame.transform import scale
GRAVITY_ACCELERATION = 20
MAX_VERTICAL_SPEED = 300


class Entity(Sprite):
    def __init__(self, image_name: str, position: tuple[int, int],
                 size: tuple[int, int], velocity: tuple[int, int],
                 *groups: AbstractGroup):
        super().__init__(*groups)
        self.on_ground = False
        self.image, self.velocity = scale(load_image(image_name), size), Vector(*velocity)
        self.rect, self.position = self.image.get_rect().move(*position), Vector(*position)

    def update(self, *args, **kwargs) -> None:
        if 'event' in kwargs:
            self._handle_event(kwargs['event'])
        if 'duration' in kwargs:
            self._update_duration(kwargs['duration'])

    def _handle_event(self, event) -> None:
        pass

    def _update_duration(self, duration: float) -> None:
        if self.on_ground:
            self.velocity.y = 0
        else:
            self.velocity.y = min(self.velocity.y + GRAVITY_ACCELERATION * duration, MAX_VERTICAL_SPEED)
        self.position += self.velocity * duration
        self.__update_rect()

    def set_position(self, x, y):
        self.position.x, self.position.y = x, y
        self.__update_rect()

    def __update_rect(self):
        self.rect.x, self.rect.y = map(int, [self.position.x, self.position.y])

