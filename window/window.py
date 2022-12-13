import time
import pygame
WINDOW_SIZE = 500, 500
WINDOW_TITLE = "Yandex Game"
WINDOW_FPS = 60


class Window:
    def __init__(self):
        self.start = self.end = time.time()
        self.background_color = pygame.Color(0, 0, 0)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.running = True
        pygame.display.set_caption(WINDOW_TITLE)

    def update(self):
        duration = self.end - self.start

    @staticmethod
    def display():
        pygame.display.flip()

    def clear(self):
        self.screen.fill(self.background_color)

    def draw(self):
        pass

    def quit(self):
        self.running = False

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

    def handle_events(self):
        for event in pygame.event.get():
            self.handle_event(event)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()