from lib import *
from hex import * 
from bld import *


# Game loop
while True:


    # Handle input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            proper_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                proper_exit()


    # Draw something to the screen buffer
    screen.fill(COLOURS["sea"])
    base_map_color_test(screen)
    
    [draw_house(screen, hex_corner(get_center(), i))
            for i in range(6)]
    [draw_bar(screen, hex_middle(get_center(), i), i)
            for i in range(6)]

    # Display the new frame and wait for next game loop
    pygame.display.flip()
    clock.tick(FPS)
