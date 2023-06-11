#!/usr/bin/python3

from my_class import Direction, Screen, Screen_enum, is_opposite
import random
import pygame

class Snake:
    def __init__(self, x, y):
        self.dimensions = (x, y)
        self.score = 0
        self.head_life = 3
        self.map = [[0 for i in range(x)] for j in range(y)]
        self.direction = Direction.Right
    
    def update(self, events):
        old_map = self.copy_map()
        old_direction = self.direction
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_z:
                    self.direction = Direction.Up
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.direction = Direction.Down
                if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    self.direction = Direction.Left
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.direction = Direction.Right
                if event.key == pygame.K_ESCAPE:
                    Screen.screen = Screen_enum.Exit
                    return
        if is_opposite(self.direction, old_direction):
            self.direction = old_direction
        head = self.search_head()

        if self.direction == Direction.Up and head[0] - 1 >= 0:
            self.map[head[0] - 1][head[1]] = self.head_life + 1
        elif self.direction == Direction.Up:
            Screen.screen = Screen_enum.Over

        if self.direction == Direction.Down and head[0] + 1 < self.dimensions[1]:
            self.map[head[0] + 1][head[1]] = self.head_life + 1
        elif self.direction == Direction.Down:
            Screen.screen = Screen_enum.Over

        if self.direction == Direction.Left and head[1] - 1 >= 0:
            self.map[head[0]][head[1] - 1] = self.head_life + 1
        elif self.direction == Direction.Left:
            Screen.screen = Screen_enum.Over

        if self.direction == Direction.Right and head[1] + 1 < self.dimensions[0]:
            self.map[head[0]][head[1] + 1] = self.head_life + 1
        elif self.direction == Direction.Right:
            Screen.screen = Screen_enum.Over

        self.kill_cell()
        self.did_eat_or_die(old_map)
    
    def copy_map(self):
        res = []
        for tab in self.map:
            res.append(tab.copy())
        return res
    
    def kill_cell(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] > 0:
                    self.map[y][x] -= 1
    
    def did_eat_or_die(self, old_map):
        pos = self.search_head()
        if old_map[pos[0]][pos[1]] == -1:
            self.eat()
        if old_map[pos[0]][pos[1]] > 1:
            Screen.screen = Screen_enum.Over


    def eat(self):
        self.score += 1
        self.head_life += 1
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] > 0:
                    self.map[y][x] += 1
        self.place_apple()

    def search_head(self):
        max = (0, 0)
        max_value = 0
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] > max_value:
                    max = (y, x)
                    max_value = self.map[y][x]
        return max
    
    def place_apple(self):
        place = False
        while not place:
            random_x = random.randint(0, self.dimensions[0] - 1)
            random_y = random.randint(0, self.dimensions[1] - 1)
            if self.map[random_y][random_x] == 0:
                self.map[random_y][random_x] = -1
                place = True
    def place_snake(self):
        y = self.dimensions[1] // 2
        x = self.dimensions[0] // 4
        self.map[y][x] = self.head_life