#!/usr/bin/python3

from dataclasses import dataclass
from enum import Enum

@dataclass
class Color:
    background = (0, 0, 0)
    head = (255, 255, 0)
    body = (0, 255, 0)
    apple = (255, 0, 0)

class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

def is_opposite(d1: Direction, d2: Direction):
    if d1 == Direction.Up and d2 == Direction.Down:
        return True
    if d1 == Direction.Down and d2 == Direction.Up:
        return True
    if d1 == Direction.Left and d2 == Direction.Right:
        return True
    if d1 == Direction.Right and d2 == Direction.Left:
        return True
    return False


class Screen(Enum):
    Main = 0
    Game = 1
    Over = 2