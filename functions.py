import random, pygame, sys
from Constants import *

def random_color():
    list_of_colors = [ red, blue, yellow]
    return random.choice(list_of_colors)

def note_positions(): #to make the lines where the notes will fall down from
    pass


def draw_notes (): #draws the notes
    pass




def main_menu():
    screen.fill(black)
    menu_rects.clear()


    for i, item in enumerate(menu_items):
        text_surface = font.render(item, True, black)
        text_rect = text_surface.get_rect(center=(screen_width // 2,( screen_height // 2 - total //2 ) + i * 120))


        mouse_pos = pygame.mouse.get_pos()
        if text_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, highlight, text_rect.inflate(20, 10))
        else:
            pygame.draw.rect(screen, gray, text_rect.inflate(20, 10))


        screen.blit(text_surface, text_rect)
        menu_rects.append(text_rect)  # Store the rects for interaction

    pygame.display.flip()

def song_selection():
    screen.fill(black)
    text_surface = font.render("Select a song", True, black)
    text_rect = text_surface.get_rect(center = (screen_width // 2, screen_height // 2 ))
    screen.blit(text_surface, text_rect)



def settings_screen():
    pass