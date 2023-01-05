import sys
import pygame

from screen_components import SceneManager
from window import Window


def start():
    pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    start()
    scene_manager = SceneManager()
    window = Window(scene_manager)
    window.opening()
    window.main_loop()
    window.ending()
    terminate()
