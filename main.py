import pygame
from window import Window

if __name__ == '__main__':
    pygame.init()
    window = Window()
    window.main_loop()
    pygame.quit()
