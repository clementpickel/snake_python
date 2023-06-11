#!/usr/bin/python3

from my_class import Screen, Screen_enum, Color
import pygame

class Help:
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
        window.fill(Color.help_background)
        font = pygame.font.Font(None, 30)
        text_surface = font.render("You control a snake whose goal is to grow as big as possible.", True, Color.white)
        text_x = 100
        text_y = 600 // 2 - text_surface.get_height() // 2
        window.blit(text_surface, (text_x, text_y))

        font = pygame.font.Font(None, 30)
        text_surface = font.render("To move, use the zqsd keys or the arrow keys", True, Color.white)
        text_x = 100
        text_y = 600 // 2 - text_surface.get_height() // 2 + 40
        window.blit(text_surface, (text_x, text_y))

        pygame.display.flip()
