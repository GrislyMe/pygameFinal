import pygame
import random
import sys
sys.path.append(".")
from bullet import *

class enemy(pygame.sprite.Sprite):
    def __init__(self, pos : list):
        pygame.sprite.Sprite.__init__(self)
        self.__current = pygame.math.Vector2(tuple(pos))
        self.__movement = 0.3
        self.hitBox = []
        self.rect = []

    def update(self):
        direction = random.randint(0, 100)
        if direction == 59:
            self.__movement *= -1
        if 0 < self.__current[0] + self.__movement < 800:
            self.__current += (self.__movement, 0)
            self.rect.center = self.__current
            self.hitBox.center = self.__current

    def fire(self, direction):
        temp = direction - self.__current
        temp = temp.normalize()
        return bulletFromNpc(self.__current, temp, [800, 600])

class pineApplePizza(enemy):
    def __init__(self, pos : list):
        super().__init__(pos)
        self.__setImg()
        self.__setHitBox()

    def __setImg(self):
        self.imgPath = "./png/enemy1.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = pygame.Rect(self._enemy__current, (30, 30))

class boss(enemy, pygame.sprite.Sprite):
    def __init__(self, pos : list):
        super().__init__(pos)
        self.__setImg()
        self.__setHitBox()

    def __setImg(self):
        self.imgPath = "./png/boss1.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = pygame.Rect(self._enemy__current, (30, 20))

    def fire(self):
        return beamFromNpc(self._enemy__current)
