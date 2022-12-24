import sys
import pygame
from window import Window


def start():
    pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    start()
    window = Window()
    window.opening()
    window.main_loop()
    window.ending()
    terminate()
