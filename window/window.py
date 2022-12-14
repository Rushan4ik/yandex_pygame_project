import time
import pygame
from screen_components import SceneManager

WINDOW_SIZE = 500, 500
WINDOW_TITLE = "Yandex Game"
WINDOW_FPS = 60


class Window:

    def __init__(self, scene_manager: SceneManager):
        self.start = self.end = time.time()
        self.running, self.background_color = True, pygame.Color(77, 143, 172)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.scene_manager = scene_manager
        self.scene_manager.window_size = WINDOW_SIZE
        pygame.display.set_caption(WINDOW_TITLE)

    def init_components(self):
        self.scene = self.scene_manager.get_current_scene()

    def update(self):
        duration = self.end - self.start
        self.scene.update(duration)

    @staticmethod
    def display():
        pygame.display.flip()

    def clear(self):
        self.screen.fill(self.background_color)

    def draw(self):
        self.scene.draw(self.screen)

    def main_loop(self):
        timer = pygame.time.Clock()
        while self.running:
            self.scene = self.scene_manager.get_current_scene()
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
        else:
            self.scene.handle_event(event)

    def opening(self):
        pass

    def ending(self):
        pass
