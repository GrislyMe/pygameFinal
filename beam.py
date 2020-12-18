import pygame

# not wuite sure how to do this one
# it just here, but not functioning

class beam(pygame.sprite.Sprite):
    #initialize start end direction
    def __init__(self, startPos : list, vec2d : list):
        pygame.sprite.Sprite.__init__(self)
        self.__current = pygame.math.Vector2(startPos)
        self.__dir = pygame.math.Vector2(vec2d)
        self.__setImg()

    # allow you to use print(s) = [current[0], current[1]]
    # after bullet(...)
    def __repr__(self):
        return repr(self.__current)

    def __setImg(self):
        self.imgPath = "./png/defaultBullet2.png"
        self.image = pygame.image.load(self.imgPath)
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(self.__current, (9, 9))

    # move nullet alone with the vector
    def update(self):
        self.__current += self.__dir
        self.rect.center = self.__current
        self.hitbox.center = self.__current

    # return true if bullet reach the end pos
    def isEnd(self):
        temp = self.__end[0] - self.__current[0]
        if temp * self.__dir[0] < 0:
            self.__dir = [0, 0]
            return True
        return False


    # define the behavior when bullet reach end pos
    def __del__(self):
        return

# class flower(bullet):
