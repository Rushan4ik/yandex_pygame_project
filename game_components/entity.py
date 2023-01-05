from pygame.sprite import Sprite, AbstractGroup
from json import load
from game_components.animation import Animation
from math_components import Vector
from pygame.mask import from_surface
json_value = load(open('configs.json'))
GRAVITY_ACCELERATION = json_value['GRAVITY_ACCELERATION']
MAX_VERTICAL_SPEED = json_value['MAX_VERTICAL_SPEED']


class Entity(Sprite):
    def __init__(self, image_name: str, frame_count: int, animation_speed: float,
                 position: tuple[int, int], size: tuple[int, int], velocity: tuple[int, int],
                 *groups: AbstractGroup):
        super().__init__(*groups)
        self.on_ground, self.image_name = False, image_name
        self.velocity, self.animation = Vector(*velocity), Animation(image_name, size, frame_count, animation_speed)
        self.animation.running = False
        self.image = self.animation.get_current_frame()
        self.rect, self.position = self.image.get_rect().move(*position), Vector(*position)
        self.mask = from_surface(self.image)

    def update(self, *args, **kwargs) -> None:
        if 'event' in kwargs:
            self._handle_event(kwargs['event'])
        if 'duration' in kwargs:
            self._update_duration(kwargs['duration'])

    def _update_duration(self, duration: float) -> None:
        self.animation.update(duration)
        self.image = self.animation.get_current_frame()
        if self.on_ground:
            self.velocity.y = 0
        else:
            self.velocity.y = min(self.velocity.y + GRAVITY_ACCELERATION * duration, MAX_VERTICAL_SPEED)
        self.position += self.velocity * duration
        self.__update_rect()

    def set_position(self, x: float, y: float) -> None:
        self.position.x, self.position.y = x, y
        self.__update_rect()

    def __update_rect(self) -> None:
        self.rect.x, self.rect.y = map(int, [self.position.x, self.position.y])

    def _handle_event(self, event) -> None:
        pass
