import pygame

class eventHandler():
    def __init__(self):
        self.__dir = {"left":False, "right":False, "up":False, "down":False}
        self.__isPause = False

    def eventReceive(self):
        # while not pygame.key.get_focused():
        #    pass
        for event in pygame.event.get():
            if self.__checkPause(event):
                continue
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                self.__checkUserKeyUp(event.key)
            elif event.type == pygame.KEYDOWN:
                self.__checkUserKeyDown(event.key)

    def __checkPause(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.__togglePause()
                return True
        elif not pygame.key.get_focused():
            self.__togglePause()
        return False

    def __togglePause(self):
        if self.__isPause:
            self.__isPause = False
        else :
            self.__pause()

    def __pause(self):
        self.__isPause = True
        while self.__isPause:
            self.eventReceive()

    def __checkUserKeyDown(self, key):
        if key == pygame.K_UP or key == pygame.K_w:
            self.__dir["up"] = True
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.__dir["down"] = True
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.__dir["right"] = True
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.__dir["left"] = True

    def __checkUserKeyUp(self, key):
        if key == pygame.K_UP or key == pygame.K_w:
            self.__dir["up"] = False
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.__dir["down"] = False
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.__dir["right"] = False
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.__dir["left"] = False

    def getMomentum(self):
        dx = 0
        dy = 0

        if self.__dir["left"]:
            dx += -3
        if self.__dir["right"]:
            dx += 3
        if self.__dir["up"]:
            dy += -2
        if self.__dir["down"]:
            dy += 2
        return (dx, dy)


