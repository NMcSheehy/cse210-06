import pygame
pygame.init()
import random

def main():
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
    
    window = Window(1000, 750, "Zombie Infection!", (255,255,255))
    
    game = Director(60)
    
    game.start(window)

class Director():
    def __init__(self, FPS):
        self.playing = True
        self.FPS = FPS
        
        self.clock = pygame.time.Clock()
    
    def start(self, window):
        while self.playing:
            self.clock.tick(self.FPS)
            level = 1
            match level:
                case 1:
                    complete_1 = False
                    
                    if complete_1 == True:
                        level += 1
                case 2:
                    complete_2 = False
                    
                    if complete_2 == True:
                        level += 1
                case 3:
                    complete_3 = False
                    
                    if complete_3 == True:
                        pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False   
                
            window.draw()

class Window():
    def __init__(self, width, height, name, background):
        self.width = width
        self.height = height
        self.name = name
        self.background = background
        
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        
    def draw(self):
        self.display.fill(self.background)
        
        pygame.display.update()

class NPC():
    def __init__(self, path, width, height, x, y, speed, infection_rate):
        self.path = path
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.infection_rate = infection_rate
    
    def move(self):
        pass
    
    def infection(self):
        pass

class Zombie(NPC):
    def __init__(self):
        pass

    def move(self): 
        pass

    def infection(self):
        pass    

class Villager(NPC):
    def __init__(self):
        pass

    def move(self): 
        pass

    def infection(self):
        pass
    
    def change(self):
        pass


if __name__ == '__main__':
    main()