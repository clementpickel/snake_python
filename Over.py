#!/usr/bin/python3

import pygame
from my_class import Screen_enum, Color, Screen

class Over:
    def __init__(self):
        pass

    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                Screen.screen = Screen_enum.Main
    
    def draw(self, window: pygame.Surface):
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Game Over", True, Color.red)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2
        window.blit(text_surface, (text_x, text_y))

        font = pygame.font.Font(None, 20)
        text_surface = font.render("Press any key to go back to menu", True, Color.white)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2 + 40
        window.blit(text_surface, (text_x, text_y))

        pygame.display.flip()
        