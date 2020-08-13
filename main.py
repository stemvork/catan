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
                STATE["turn"] += 1
            elif event.key == pygame.K_n:
                STATE.update(initial_state())


    # Draw something to the screen buffer
    screen.fill(COLOURS["bg"])
    base_map_color_test(screen)
    base_structs(screen)
    draw_robber(screen, get_center())

    draw_playing(screen)
    draw_turn(screen)


    # Display the new frame and wait for next game loop
    pygame.display.flip()
    clock.tick(FPS)
