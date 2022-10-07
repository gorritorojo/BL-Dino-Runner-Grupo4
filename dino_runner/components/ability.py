from pygame.sprite import Sprite
from components.dinosaurio import Dinosaur
from utils.constants import SCREEN_WIDTH, RUNNING_SHIELD, SHIELD
import random


position_y = random.randrange(50, 250, 20)


class Ability(Sprite):
    def __init__(self):
        self.dino_change = RUNNING_SHIELD[0]
        self.image = SHIELD
        self.ability_rect = self.image.get_rect()
        self.other_position = SCREEN_WIDTH
        self.position_ability_x = self.other_position 
        self.position_ability_y = position_y
        self.count = range(1, 100)

    def change_dino(self, game,):
         if game.dino.dino_rect.colliderect(self.ability_rect):
            pass
                  
    def draw(self, screen):
        screen.blit(self.image, (self.position_ability_x, self.position_ability_y))

    def movimiento(self):
        self.position_ability_x -= 10


        