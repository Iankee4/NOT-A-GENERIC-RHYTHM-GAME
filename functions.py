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
    pygame.init()
    pygame.display.set_caption("Not A Generic Rhythm Game")
    screen.fill(black)
    menu_rects.clear()
    for i in range(len(menu_items)):
        text_top = pygame.font.Font(None, 30)
        text = text_top.render(menu_items[i], True, black)
        text_box = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)


        mouse_pos = pygame.mouse.get_pos()

        if text_box.collidepoint(mouse_pos):
            pygame.draw.rect(screen, gray, text_box)

        else:
            pygame.draw.rect(screen, gray , text_box)

        screen.blit(text, text_box)
        menu_rects.append(text_box)


    pygame.display.update()