from functions import *


while True:
    main_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(menu_rects):
                if rect.collidepoint(event.pos):
                    if menu_items[i] == "Play":
                        pass
                        #level selection screen should open


                    elif menu_items[i] == "Settings":
                        pass
                       # menu screen that should let you change keybind and stuff
                    elif menu_items[i] == "Exit":
                        quit()



