import time
import pygame
from game_components.utils import load_image


WINDOW_SIZE = 500, 500
WINDOW_TITLE = "Yandex Game"
WINDOW_FPS = 60


class Window:

    def __init__(self, size=WINDOW_SIZE, background_fn=None):
        self.start = self.end = time.time()
        self.running = True
        if background_fn:
            self.background = pygame.transform.scale(load_image(background_fn), size)
        else:
            self.background = pygame.display.set_mode(size)
            self.background.fill(pygame.color.Color('black'))
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.screen.blit(self.background, (0, 0))
        self.init_components()
        pygame.display.set_caption(WINDOW_TITLE)

    def init_components(self):
        pass

    def update(self):
        duration = self.end - self.start

    @staticmethod
    def display():
        pygame.display.flip()

    def clear(self):
        self.screen.blit(self.background, (0, 0))

    def draw(self):
        pass

    def main_loop(self):
        timer = pygame.time.Clock()
        while self.running:
            self.handle_events()
            self.clear()
            self.end = time.time()
            self.update()
            self.draw()
            self.display()
            timer.tick(WINDOW_FPS)
            self.start = self.end

    def quit(self):
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()

    def opening(self):
        pass

    def ending(self):
        pass

