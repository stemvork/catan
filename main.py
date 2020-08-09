from lib import *


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
    screen.fill(BG)
    pygame.draw.rect(screen, COLOURS[0], (15, 15, 15, 15))


    # Display the new frame and wait for next game loop
    pygame.display.flip()
    clock.tick(FPS)
