import pygame
pygame.init()
import random

def main():
    window = Window()
    
    game = Director(60)
    
    game.start(window)

class Director():
    def __init__(self, FPS):
        self.playing = True
        
        self.clock = pygame.time.Clock()
    
    def start(self, window):
        while self.playing:
            self.clock.tick(self.FPS)
            level = 1
            match level:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass

class Window():
    pass

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