# Import modules
import pygame
import random

pygame.init()

# Define Variables

title = 'cse210-06 Zombie Simulator'

window_height = 500
window_width = 500

fps = 30

# Colors
yt_darkmode1 = (24,24,24)
yt_darkmode2 = (33,33,33)
yt_darkmode3 = (61,61,61)

zombie_color = (69,107,62)
villager_color = (96,163,217)

bg_color = (200, 200, 200)

# Object variables
radius = 7
thickness = 3
speed = 1

class Object():
    def __init__(self, x, y, radius, thickness, speed) -> None:
        self.x = x 
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.speed = speed

    def move(self):
        self.x += random.randint(-speed, speed)
        self.y += random.randint(-speed, speed)

class Zombie(Object):
    def __init__(self, x, y, radius, thickness, speed, fear) -> None:
        super().__init__(x, y, radius, thickness, speed)
        self.fear = fear

    def move(self):
        x, y = pygame.mouse.get_pos()

        self.x += random.randint(-speed, speed)
        self.y += random.randint(-speed, speed)

class Villager(Object):
    def __init__(self, x, y, radius, thickness, speed) -> None:
        super().__init__(x, y, radius, thickness, speed)

    def move(self):
        self.x += random.randint(-speed, speed)
        self.y += random.randint(-speed, speed)

def main():
    # setup the game window
    display = pygame.display.set_mode((window_width, window_height))
    display.fill(bg_color)
    running = True
    clock = pygame.time.Clock()

    # Import classes
    
    zombies = []
    for _ in range(10):
        zombies.append(Zombie(window_width // 3, window_height // 2, radius, thickness, 5, 50))

    villagers = []
    for _ in range(10):
        villagers.append(Villager(window_width // 1.5, window_height // 2, radius, thickness, 5))


    while running:
        # Clock the FPS
        clock.tick(fps)

        # Track the events
        for event in pygame.event.get():
            # Event: Quit game
            if event.type == pygame.QUIT:
                running = False

        # Update Game
        for zombie in zombies:
            zombie.move()

        for villager in villagers:
            villager.move()

        # Draw Display (bottom layer to top)
        display.fill(bg_color)

        # Draw Villagers
        for villager in villagers:
            pygame.draw.circle(display, villager_color, (villager.x, villager.y), villager.radius, villager.thickness)

        # Draw Zombie
        for zombie in zombies:
            pygame.draw.circle(display, zombie_color, (zombie.x, zombie.y), zombie.radius, zombie.thickness)

        # Update Window
        pygame.display.set_caption(title)
        pygame.display.update()

if __name__ == '__main__':
    main()