from game_components.utils import load_image
from pygame.transform import flip, scale


class Animation:
    def __init__(self, image: str, size, frame_count: int, speed: float):
        self.frames = [scale(load_image(f'{image}-{i + 1}.png'), size)
                       for i in range(frame_count)]
        self.speed, self.running = speed, True
        self.reflect_image, self.frame_count = False, frame_count
        self.current = self.time = 0

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
