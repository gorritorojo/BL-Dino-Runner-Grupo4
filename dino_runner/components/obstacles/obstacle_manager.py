import pygame
from components import game
import random
from components.obstacles.cactus import Cactus
from utils.constants import (
    LARGE_CACTUS, SMALL_CACTUS
    )

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(1, 2)
            if cactus_size == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif cactus_size == 2:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update()
            #if obstacle.image_rect.x < -obstacle.image_rect.width:
            #    self.obstacles.pop()
            if game.dino.dino_rect.colliderect(obstacle.image_rect):
                pygame.time.delay(100)
                game.death_count += 1
                self.obstacles.pop()
                if game.death_count == 5:
                    game.playing = False
                print(game.death_count)
                break