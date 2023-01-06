import os
import sys
import pygame
from json import load, dump


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"File '{fullname}' not exists")
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def get_configs_param(name: str) -> float:
    json_value = load(open('configs.json', 'r'))
    return json_value[name]


def set_configs_param(name: str, value: float) -> None:
    json_value = load(open('configs.json', 'r'))
    json_value[name] = value
    dump(json_value, open('configs.json', 'w'))
