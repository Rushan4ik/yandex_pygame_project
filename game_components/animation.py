from game_components.utils import load_image
from pygame.transform import flip, scale


class Animation:
    def __init__(self, image: str, size, n: int, speed):
        self.frames = [scale(load_image(f'{image}-{i + 1}.png'), size) for i in range(n)]
        self.speed, self.running = speed, True
        self.reflect_image = False
        self.current = self.time = 0
        self.frame_count = n

    def stop(self):
        self.running = False

    def start(self):
        self.running = True

    def update(self, delta: float):
        if not self.running:
            return
        self.time += delta
        while self.time > self.speed:
            self.time -= self.speed
            self.current += 1
        self.current %= self.frame_count

    def get_current_frame(self):
        if self.reflect_image:
            return flip(self.frames[self.current], True, False)
        return self.frames[self.current]

    def reflect(self):
        self.reflect_image = not self.reflect_image
