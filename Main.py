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
                        song_selection()
                        print("play")


                    elif menu_items[i] == "Settings":
                        print("settings")
                        settings_screen()

                       # menu screen that should let you change keybind and stuff
                    elif menu_items[i] == "Exit":
                        quit()



