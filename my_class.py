#!/usr/bin/python3

from dataclasses import dataclass
from enum import Enum

@dataclass
class Color:
    background = (0, 0, 0)
    head = (255, 255, 0)
    body = (0, 255, 0)
    apple = (255, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    main_background = (0, 100, 0)
    help_background = (0, 0, 100)

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


class Screen_enum(Enum):
    Main = 0
    Game = 1
    Over = 2
    Help = 3
    Exit = 4

@dataclass
class Screen:
    screen: Screen_enum = Screen_enum.Main

# class Screen:
#     __instance = None

#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#             cls.__instance.current_screen = Screen_enum.Main  # Définir l'écran initial
#         return cls.__instance

#     def set_screen(self, screen):
#         self.current_screen = screen

#     def get_screen(self):
#         return self.current_screen