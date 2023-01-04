import pygame
from pygame.sprite import AbstractGroup

from game_components import Entity
from game_components.animation import Animation


class Player(Entity):
    IMAGE_NAME = 'tux'
    CONTROL_KEYS = {
        'jump':  {pygame.K_UP},
        'left':  {pygame.K_LEFT},
        'right': {pygame.K_RIGHT}
    }
    PLAYER_SPEED = 50
    JUMP_FORCE = 30
    ANIMATION_SPEED = 0.3
    FRAME_COUNT = 14

    def __init__(self, position: tuple[int, int], size: tuple[int, int],
                 velocity: tuple[int, int], *groups: AbstractGroup):
        super().__init__(Player.IMAGE_NAME, Player.FRAME_COUNT, Player.ANIMATION_SPEED,
                         position, size, velocity, *groups)
        self.right = self.left = False
        self.live_count = 3

    def _handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            self.__handle_press_key(event.key, True)
        if event.type == pygame.KEYUP:
            self.__handle_press_key(event.key, False)

    def __handle_press_key(self, key, press: bool) -> None:
        if key in self.CONTROL_KEYS['jump'] and press:
            self.jump()
            return
        if key in self.CONTROL_KEYS['left']:
            self.left = press
        if key in self.CONTROL_KEYS['right']:
            self.right = press
        self.__handle_velocity()

    def jump(self) -> None:
        if self.on_ground:
            self.velocity.y = -Player.JUMP_FORCE
            self.on_ground = False

    def __handle_velocity(self) -> None:
        self.velocity.x = 0
        if self.right:
            self.velocity.x += +Player.PLAYER_SPEED
        if self.left:
            self.velocity.x += -Player.PLAYER_SPEED
        self.animation.reflect_image = self.velocity.x < 0
        self.animation.running = self.velocity.x != 0
