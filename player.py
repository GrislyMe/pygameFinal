import sys
import pygame
sys.path.append(".")

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 5
        self.atk = 5
        self.__current = pygame.math.Vector2(400, 300)
        self.__setImage__()

    def __setImage__(self):
        self.imgPath = "./png/player1.png"
        self.image = pygame.image.load(self.imgPath)
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.__current, (9, 9))

    def update(self, movement):
        self.__current += movement
        self.rect.center = self.__current
        self.hitbox.center = self.__current

