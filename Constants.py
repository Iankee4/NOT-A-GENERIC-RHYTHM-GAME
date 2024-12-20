import pygame
pygame.init()
fps = 60
bg_color = pygame.Color('black')
screen_width = 600
screen_height =600
player_speed = 0
screen = pygame.display.set_mode((screen_width, screen_height))
green = pygame.Color('green')
red = pygame.Color('red')
blue = pygame.Color('blue')
yellow = pygame.Color('yellow')
white = pygame.Color('white')
black = pygame.Color('black')
gray = pygame.Color('gray')

font = pygame.font.Font(None, 125)
highlight = (150, 150, 150)
menu_items = ["Play", "Settings","Exit"]
menu_rects = []
total = len(menu_items) * 120