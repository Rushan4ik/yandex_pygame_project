import sys
import pygame
from window import Window
from game_components.start_screen import Start_Screen


def start():
    pygame.init()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    start()
    '''window = Window()
    window.opening()
    window.main_loop()
    window.ending()'''
    Start_screen = Start_Screen()
    Start_screen.show()
    terminate()

