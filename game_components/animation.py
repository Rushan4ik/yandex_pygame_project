from game_components.utils import load_image


class Animation:
    def __init__(self, image: str, n: int, speed):
        self.frames = [load_image(f'{image}-{i + 1}.png') for i in range(n)]
        self.speed, self.running = speed, True
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
        return self.frames[self.current]
