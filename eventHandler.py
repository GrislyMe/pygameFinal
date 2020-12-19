import pygame

class eventHandler():
    def __init__(self):
        self.__dir = {"left":False, "right":False, "up":False, "down":False}

    def eventReceive(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                self.__checkUserKeyUp(event)
            elif event.type == pygame.KEYDOWN:
                self.__checkUserKeyDown(event)

    def __checkUserKeyDown(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__dir["up"] = True
            elif event.key == pygame.K_DOWN:
                self.__dir["down"] = True
            if event.key == pygame.K_RIGHT:
                self.__dir["right"] = True
            elif event.key == pygame.K_LEFT:
                self.__dir["left"] = True

    def __checkUserKeyUp(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.__dir["up"] = False
            elif event.key == pygame.K_DOWN:
                self.__dir["down"] = False
            if event.key == pygame.K_RIGHT:
                self.__dir["right"] = False
            elif event.key == pygame.K_LEFT:
                self.__dir["left"] = False

    def getMomentum(self):
        dx = 0
        dy = 0

        if self.__dir["left"]:
            dx += -2
        if self.__dir["right"]:
            dx += 2
        if self.__dir["up"]:
            dy += -2
        if self.__dir["down"]:
            dy += 2
        return (dx, dy)


