from lib import *
from game import * 


current = 0


# Game loop
while True:


    # Handle input from user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            proper_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                proper_exit()
            elif event.key == pygame.K_SPACE:
                if current < 18:
                    current += 1
                else:
                    current = 0


    # Draw something to the screen buffer
    screen.fill(COLOURS["sea"])
    base_map_color_test(screen)
    base_structs(screen)


    # Display the new frame and wait for next game loop
    pygame.display.flip()
    clock.tick(FPS)
