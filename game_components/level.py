from pygame.sprite import Group

from game_components import Player, Wall


class Level:
    def __init__(self, walls: list[Wall], spawn_point: tuple[int, int]):
        self.walls = Group()
        self.walls.add(walls)
        self.spawn_point = spawn_point
        self.player_group = Group()
        self.player = Player(self.spawn_point, (32, 31), (0, 0), self.player_group)

    def update(self, delta: float) -> None:
        self.player.update(duration=delta)
        self.player.on_ground = False
        for wall in self.walls:
            wall.handle_entity(self.player)

    def handle_event(self, event):
        self.player.update(event=event)

    def restart(self):
        self.player.set_position(*self.spawn_point)
        self.player.live_count -= 1
