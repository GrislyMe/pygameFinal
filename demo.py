import sys
sys.path.append(".")
from bullet import bullet
from player import player
import pygame
import random

# the basic demo about how to use all this function

# Event handler
def eventHandler(event):
    dx = 0
    dy = 0
    # allow user to close the window by click th X on top right
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    # input detect
    elif event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dy += -2
        if keys[pygame.K_DOWN]:
            dy += 2
        if keys[pygame.K_LEFT]:
            dx += -2
        if keys[pygame.K_RIGHT]:
            dx += 2

    return (dx, dy)

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

clock = pygame.time.Clock()
frame = 1
while True:
    # fps = 60
    # this while loop only run 60 times a sec
    clock.tick(60)
    frame += 1
    for event in pygame.event.get():
        movement = eventHandler(event)
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

    # keep track current fps
    if frame == 59:
        frame = 1
# bye bye
pygame.quit()
