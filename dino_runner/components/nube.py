from pygame.sprite import Sprite
from utils.constants import CLOUD

class Cloud(Sprite):

    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_x = 500 
        self.cloud_y = 200

    def draw(self, screen):
        screen.blit(self.image, (self.cloud_x, self.cloud_y))
        self.cloud_rect = self.image.get_rect()

    