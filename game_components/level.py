from pygame.sprite import Group

from game_components import Player, Wall, Camera, Entity
from game_components.finish import Finish
from game_components.spike import Spike


class Level:
    def __init__(self, window_size: tuple[int, int],
                 walls: list[Wall], spikes: list[Spike],
                 entities: list[Entity], spawn_point: tuple[int, int],
                 finishes: list[Finish]):
        self.running, self.result = True, 0
        self.entities, self.walls, self.spikes, self.finishes = [Group() for _ in range(4)]
        self.entities.add(entities)
        self.walls.add(walls)
        self.spikes.add(spikes)
        self.finishes.add(finishes)
        self.spawn_point = spawn_point
        self.player_group = Group()
        self.player = Player(self.spawn_point, (32, 31), (0, 0), self.player_group)
        self.camera = Camera(window_size)

    def update(self, delta: float) -> None:
        self.result += delta
        self.player.update(duration=delta)
        self.player.on_ground = False
        for wall in self.walls:
            wall.handle_entity(self.player)
        for spike in self.spikes:
            if spike.handle_entity(self.player):
                self.restart()
        for finish in self.finishes:
            if finish.handle_entity(self.player):
                self.running = False

    def handle_event(self, event):
        self.player.update(event=event)

    def restart(self):
        self.result = 0
        self.player.live_count -= 1
        self.player.set_position(*self.spawn_point)

    def draw(self, screen):
        self.walls.draw(screen)
        self.entities.draw(screen)
        self.player_group.draw(screen)

    def get_result(self) -> float:
        return self.result

