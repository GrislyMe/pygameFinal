import sys
sys.path.append(".")
from bullet import bullet
from player import player
import pygame
import random
import time

# this file is used to test hitbox

pygame.init()


winSize = (800, 600)
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("Test")

temp = player()

projectile = pygame.sprite.Group()
temp.update(5, 5)
projectile.add(temp)
projectile.draw(screen)
pygame.draw.rect(screen, (255, 0, 0), temp.hitbox, 1)
pygame.display.update()

time.sleep(30)

pygame.quit()
