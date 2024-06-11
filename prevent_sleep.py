import pygame
import time

def prevent_sleep():
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((1, 1))
    pygame.display.set_caption('Prevent Sleep')
    pygame.display.iconify()

    # Fill the screen with black color
    screen.fill((0, 0, 0))
    pygame.display.update()

    try:
        # Main loop to keep the window active
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Update the display periodically to keep the system awake
            pygame.display.flip()
            time.sleep(1)  # Adjust the sleep time if necessary

    except KeyboardInterrupt:
        pygame.quit()

if __name__ == "__main__":
    print("Press Ctrl+C to stop preventing sleep.")
    prevent_sleep()
