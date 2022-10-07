from components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image, rect_y=300):
        self.size = 300
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.image_rect.y = self.size

    def set_rec_y(self, rec_y):
        self.size = rec_y
        self.image_rect.y = self.size
