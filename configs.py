import pygame

# ENTITY
MAX_VERTICAL_SPEED = 300
GRAVITY_ACCELERATION = 20
# PLAYER
PLAYER_ANIMATION_SPEED = 0.3
PLAYER_CONTROL_KEYS = {
    'jump': {pygame.K_UP},
    'left': {pygame.K_LEFT},
    'right': {pygame.K_RIGHT}
}
PLAYER_SPEED = 50
PLAYER_JUMP_FORCE = 30