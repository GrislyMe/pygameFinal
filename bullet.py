import pygame

class bullet(pygame.sprite.Sprite):
    #initialize start end direction
    def __init__(self, startPos : list, vec2d : list, endPos : list):
        pygame.sprite.Sprite.__init__(self)
        self.__current = pygame.math.Vector2(startPos)
        self.__dir = pygame.math.Vector2(vec2d)
        self.__end = pygame.math.Vector2(endPos)
        self.hitBox = []
        self.rect = []
    # move nullet alone with the vector
    def update(self):
        self.__current += self.__dir
        self.rect.center = self.__current
        self.hitBox.center = self.__current

    def getPos(self):
        return self.__current

    # return true if bullet reach the end pos
    def isEnd(self):
        if self.__current.length() > self.__end.length():
            self.__dir = [0, 0]
            return True
        return False


    # define the behavior when bullet reach end pos
    def __del__(self):
        return

class bulletFromNpc(bullet):
    def __init__(self, startPos : list, vec2d : list, endPos : list):
        super().__init__(startPos, vec2d, endPos)
        self.__setImg()
        self.__setHitBox()
        self.update()

    def __setImg(self):
        self.imgPath = "./png/defaultBullet2.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = pygame.Rect(self._bullet__current, (9, 9))

class bulletFromPlayer(bullet):
    def __init__(self, startPos : list, vec2d : list):
        super().__init__(startPos, vec2d, (0, 0))
        self.__setImg()
        self.__setHitBox()
        self.update()

    def __setImg(self):
        self.imgPath = "./png/bullet2.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = pygame.Rect(self._bullet__current, (9, 9))

    def isEnd(self):
        if self._bullet__current[1] < 0:
            return True
        return False

class beamFromPlayer(bulletFromPlayer):
    def __init__(self, startPos : list):
        super().__init__(startPos, (0, 10))
        self.__setImg()
        self.__setHitBox()

    def __setImg(self):
        self.imgPath = "./png/beam1.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = self.rect

class beamFromNpc(bulletFromNpc):
    def __init__(self, startPos : list):
        super().__init__(startPos, (0, 10), (800, 600))
        self.__setImg()
        self.__setHitBox()

    def __setImg(self):
        self.imgPath = "./png/beam1.png"
        self.image = pygame.image.load(self.imgPath)

    def __setHitBox(self):
        self.rect = self.image.get_rect()
        self.hitBox = self.rect
