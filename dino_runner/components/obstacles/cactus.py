from components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.image_rect.y = 310
