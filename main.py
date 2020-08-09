from lib import *
from hex import * 


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
    # for i in range(-2, 3):
    #     for j in range(-2, 3):
    #         draw_hex(screen, (i, j))
    draw_big_hex(screen)
    base_map_color_test(screen)

    # Display the new frame and wait for next game loop
    pygame.display.flip()
    clock.tick(FPS)
