from game_components import VerticalWall, HorizontalWall
from game_components.level import Level


def get_first_level(window_size: tuple[int, int]) -> Level:
    return Level(window_size, [HorizontalWall((100, 300), (300, 50))], [], (10, 20))


def get_second_level(window_size: tuple[int, int]) -> Level:
    pass
#    return Level(window_size)


def get_third_level(window_size: tuple[int, int]) -> Level:
    pass
#    return Level(window_size)


LEVELS = [
    get_first_level,
    get_second_level,
    get_third_level,
]


def get_level(n: int, window_size: tuple[int, int]) -> Level:
    n -= 1
    if 0 <= n < len(LEVELS):
        return LEVELS[n](window_size)

