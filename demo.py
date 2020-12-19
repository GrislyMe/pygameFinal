import sys
sys.path.append(".")
from bullet import bullet
from player import player
from eventHandler import eventHandler
import pygame
import random

# the basic demo about how to use all this function

# Event handler


# window size
winSize = (800, 600)
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Demo")

# background layer
bg = pygame.Surface(winSize)
bg.fill([0, 0, 0])

bulletLayer = pygame.Surface(winSize)

# projectile spite group
# allow you to rander bullet or enemy faster
# which means make your life eazier
projectile = pygame.sprite.Group()
character = pygame.sprite.Group()

# add player in sprite
character.add(player())

handler = eventHandler()

clock = pygame.time.Clock()
movement = pygame.math.Vector2(0, 0)
frame = 1
while True:
    # fps = 60
    # this while loop only run 60 times a sec
    clock.tick(60)
    frame += 1
    handler.eventReceive()
    movement = handler.getMomentum()

    # random generate bullet pos
    tempX = random.randint(0, winSize[0] / 5)
    tempY = random.randint(0, winSize[1] / 5)
    # add one bullet each 1/6 sec
    if frame % 10 == 0:
        projectile.add(bullet([tempX, tempY], [tempX * 0.01, tempY * 0.01], [tempX * 5, tempY * 5]))


    # rander bg on screen
    # not quite sure about this part
    screen.blit(bg, (0, 0))
    projectile.draw(screen)
    character.draw(screen)
    bg.blit(bulletLayer, (0, 0))
    pygame.display.update()

    # clear screen
    bulletLayer.fill([0, 0, 0])
    # update all stuff
    for c in character:
        c.update(movement)
        # if check collide
        # if collide return index else return -1
        isHit = pygame.sprite.spritecollide(c, projectile, True)
        if len(isHit) != 0:
            print("You Die")
            sys.exit()
    for b in projectile:
        b.update()
        if b.isEnd():
            b.kill()
    movement = pygame.math.Vector2(0, 0)

    # keep track current fps
    if frame == 60:
        frame = 1
# bye bye
pygame.quit()
