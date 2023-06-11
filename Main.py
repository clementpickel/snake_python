#!/usr/bin/python3

import pygame
from my_class import Screen_enum, Color, Screen

class Main:
    def __init__(self):
        pass

    def update(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    Screen.screen = Screen_enum.Help
                    return
                if event.key == pygame.K_ESCAPE:
                    Screen.screen = Screen_enum.Exit
                    return
                Screen.screen = Screen_enum.Game
    
    def draw(self, window: pygame.Surface):
        window.fill(Color.main_background)
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Snake", True, Color.white)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2
        window.blit(text_surface, (text_x, text_y))

        font = pygame.font.Font(None, 30)
        text_surface = font.render("Press any key to start", True, Color.white)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2 + 40
        window.blit(text_surface, (text_x, text_y))

        font = pygame.font.Font(None, 30)
        text_surface = font.render("Press any 'H' for help", True, Color.white)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2 + 60
        window.blit(text_surface, (text_x, text_y))

        font = pygame.font.Font(None, 30)
        text_surface = font.render("Press any 'escape' to exit", True, Color.white)
        text_x = 800 // 2 - text_surface.get_width() // 2
        text_y = 600 // 2 - text_surface.get_height() // 2 + 80
        window.blit(text_surface, (text_x, text_y))
        pygame.display.flip()
