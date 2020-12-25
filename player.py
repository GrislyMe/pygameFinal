import sys
import pygame
sys.path.append(".")
from bullet import *

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__current = pygame.math.Vector2(400, 300)
        self.__setImg()

    def getPos(self):
        return self.__current

    def __setImg(self):
        self.imgPath = "./png/player1.png"
        self.image = pygame.image.load(self.imgPath)
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.__current, (9, 9))

    def update(self, movement):
        self.__current += movement
        self.rect.center = self.__current
        self.hitbox.center = self.__current

    def fire(self):
        return bulletFromPlayer(self.__current + [0, -20], [0, -3])

    def skill(self, movement):
        # flash
        movement *= 20
        self.__current += movement
        self.rect.center = self.__current
        self.hitbox.center = self.__current
