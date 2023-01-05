import sys
import pygame
from json import dump
from screen_components import SceneManager
from screen_components.scene_main import MainMenuScene
from window import Window
SAVE_SETTINGS = True


def start():
    if not SAVE_SETTINGS:
        dump({"MAX_VERTICAL_SPEED": 300, "GRAVITY_ACCELERATION": 50, "PLAYER_ANIMATION_SPEED": 0.3,
              "PLAYER_SPEED": 50, "PLAYER_JUMP_FORCE": 50}, open('configs.json', 'w'))
    pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    start()
    scene_manager = SceneManager()
    scene_manager.current_scene = MainMenuScene(scene_manager)
    window = Window(scene_manager)
    window.opening()
    window.main_loop()
    window.ending()
    terminate()
