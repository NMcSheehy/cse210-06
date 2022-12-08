# Import modules
import pygame
import random
import time

pygame.init()

# Define Variables

title = 'cse210-06 Zombie Simulator'

window_height = 500
window_width = 500

fps = 30

# font
font = pygame.font.Font('freesansbold.ttf', 32)

# Colors
yt_darkmode1 = (24,24,24)
yt_darkmode2 = (33,33,33)
yt_darkmode3 = (61,61,61)

zombie_color = (69,107,62)
villager_color = (96,163,217)

bg_color = (200, 200, 200)

# Object variables
level = 1
radius = 5
thickness = 3
speed = 1

# file paths
zombie_sprite_list = [
    "Brain Zombie.png",
    "Bald Zombie.png",
    "Jelly Zombie.png",
    "Flower Zombie.png",
    "Boy Zombie.png",
    "Top Hat Zombie.png",
    "Bride Zombie.png",
    "Brown Hat Zombie.png",
    "Mushroom Zombie.png",
    "Crystal Zombie.png",
    "Torch Zombie.png",
    "Cold Zombie.png",
    "Girl Zombie.png", 
    "Eye Zombie.png",
    "Fisherman Zombie.png"
]

villager_sprite_list = [
    "Miss Clause.png",
    "Black Hair.png",
    "Mushroom Man.png",
    "Scrooge.png",
    "Girl Villiger.png",
    "Wizard.png",
    "Innkeep.png",
    "Kid.png",
    "Hood.png",
    "Hard Hat.png",
    "Trump.png",
    "Old Man.png",
    "Boy Villiger.png"
]
    

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
    def __init__(self, x, y, radius, thickness, speed, fear, vision) -> None:
        super().__init__(x, y, radius, thickness, speed)
        self.fear = fear
        self.vision = vision

    def move(self, villagers):

        x, y = pygame.mouse.get_pos()

        # If the zombie is close to the mouse
        # for x Axis
        if abs(self.x - x) < self.fear and abs(self.y - y) < self.fear:
            # make the zombie run away from the mouse
            if self.x > x:
                self.x += self.speed
            if self.x < x:
                self.x -= self.speed
            if self.y > y:
                self.y += self.speed
            if self.y < y:
                self.y -= self.speed
        self.x += random.randint(-speed, speed)
        self.y += random.randint(-speed, speed)

        for villager in villagers:
            if abs(self.x - villager.x) < self.vision and abs(self.y - villager.y) < self.vision:
                if self.x < villager.x:
                    self.x += self.speed // 2
                if self.x > villager.x:
                    self.x -= self.speed // 2
                if self.y < villager.y:
                    self.y += self.speed // 2
                if self.y > villager.y:
                    self.y -= self.speed // 2
                    break
        
        if self.x > window_width - radius:
            self.x = window_width - radius
        if self.x < 0 + radius:
            self.x = 0 + radius
        if self.y > window_height - radius:
            self.y = window_height - radius
        if self.y < 0 + radius:
            self.y = 0 + radius


class Villager(Object):
    def __init__(self, x, y, radius, thickness, speed, health, vision) -> None:
        super().__init__(x, y, radius, thickness, speed)
        self.health = health
        self.alive = True
        self.vision = vision

    def move(self, zombies):

        self.x += random.randint(-speed, speed)
        self.y += random.randint(-speed, speed)

        for zombie  in zombies:
            if abs(self.x - zombie.x) < self.vision and abs(self.y - zombie.y) < self.vision:
                if self.x > zombie.x:
                    self.x += self.speed // 2
                if self.x < zombie.x:
                    self.x -= self.speed // 2
                if self.y > zombie.y:
                    self.y += self.speed // 2
                if self.y < zombie.y:
                    self.y -= self.speed // 2
                    break

        if self.x > window_width - radius:
            self.x = window_width - radius
        if self.x < 0 + radius:
            self.x = 0 + radius
        if self.y > window_height - radius:
            self.y = window_height - radius
        if self.y < 0 + radius:
            self.y = 0 + radius

    def infect(self, zombies):
        if self.health == 0:
            self.alive = False
            print('dead villager')
            zombies.append(Zombie(
            self.x, 
            self.y, 
            radius, 
            thickness, 
            5, 
            50,
            250))

        for zombie in zombies:
            if abs(self.x - zombie.x) < radius * 3 and abs(self.y - zombie.y) < radius * 3:
                self.health -= 1
                break

def main():
    # setup the game window
    display = pygame.display.set_mode((window_width, window_height))
    display.fill(bg_color)
    running = True
    clock = pygame.time.Clock()

        # load in Zombies and Villagers   

    start_time = round(time.time())
    elapsed_time = 0

    zombies = []
    for _ in range(3):
        zombies.append(Zombie(
            random.randint(0, window_width // 3), 
            random.randint(0, window_height), 
            radius, 
            thickness, 
            5, 
            50,
            250))

    villagers = []
    for _ in range(10):
        villagers.append(Villager(
            random.randint(window_width // 1.5, window_width), 
            random.randint(0, window_height),
            radius, 
            thickness, 
            5,
            10,
            250))

    while running:
        # Clock the FPS
        clock.tick(fps)

        # Track the events
        for event in pygame.event.get():
            # Event: Quit game
            if event.type == pygame.QUIT:
                running = False

        # Update Game
        
        # keep track of how long the player survives
        
        previous_time = elapsed_time
        elapsed_time = round(time.time() - start_time)


        text = font.render(str(elapsed_time), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (window_width // 2, 25)
        


        if previous_time != elapsed_time:
            print(elapsed_time)

            for zombie in zombies:
                zombie.speed += 1
                zombies.append(Zombie(
                    random.randint(0, window_width // 3), 
                    random.randint(0, window_height), 
                    radius, 
                    thickness, 
                    5, 
                    50,
                    250))
                break

        for zombie in zombies:
            zombie.move(villagers)

        count = 0
        for villager in villagers:
            
            villager.move(zombies)
            villager.infect(zombies)
            if not villager.alive:
                villagers.pop(count)
            count += 1

        if len(villagers) == 0:
            running = False
                

        # Draw Display (bottom layer to top)
        display.fill(bg_color)


        # Draw Villagers
        for villager in villagers:
            pygame.draw.circle(display, villager_color, (villager.x, villager.y), villager.radius, villager.thickness)

        # Draw Zombie
        for zombie in zombies:
            pygame.draw.circle(display, zombie_color, (zombie.x, zombie.y), zombie.radius, zombie.thickness)

        display.blit(text, textRect)

        # Update Window
        pygame.display.set_caption(title)
        pygame.display.update()
    
    print('Game Over')

if __name__ == '__main__':
    main()