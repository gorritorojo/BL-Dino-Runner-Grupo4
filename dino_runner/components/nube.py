from pygame.sprite import Sprite
from utils.constants import CLOUD, SCREEN_WIDTH
import random



position_y = random.randrange(100, 250, 10)


class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.other_position = SCREEN_WIDTH
        self.position_cloud_x = self.other_position 
        self.position_cloud_y = position_y


    def draw(self, screen):
        screen.blit(self.image, (self.position_cloud_x, self.position_cloud_y))

    def update(self):
        self.position_cloud_x -= 3
        
