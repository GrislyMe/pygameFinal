import sys
sys.path.append(".")
from bullet import *
from player import player
from enemy import *
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
#bg = pygame.Surface(winSize)
bg = pygame.image.load('./png/bg243.png').convert()

#May be no longer need
#bulletLayer = pygame.Surface(winSize)

# projectile spite group
# allow you to rander bullet or enemy faster
# which means make your life eazier
npcProj = pygame.sprite.Group()
playerProj = pygame.sprite.Group()
character = pygame.sprite.Group()
npc = pygame.sprite.Group()

# add player in sprite
character.add(player())

handler = eventHandler()

clock = pygame.time.Clock()
movement = pygame.math.Vector2(0, 0)
frame = 0
takeDown = 0
bossCount = 0
bg_Y = -600
while True:
	# fps = 60
	# this while loop only run 60 times a sec
	clock.tick(60)
	handler.eventReceive()
	movement = handler.getMomentum()

	# random generate bullet pos
	tempX = random.randint(20, winSize[0] - 20)
	tempY = random.randint(0, winSize[1] / 5)
	rand  = random.randint(0, 100)

	if rand == 5:
		npc.add(pineApplePizza([tempX, tempY]))
	if bossCount == 0 and takeDown > 10:
		bossCount += 1
		npc.add(boss([tempX, tempY]))

	# rander bg on screen
	# not quite sure about this part
	if bg_Y >= 0:
		bg_Y = -600
	else:
		bg_Y = bg_Y + 1
	screen.blit(bg,(0,bg_Y))
	npcProj.draw(screen)
	playerProj.draw(screen)
	npc.draw(screen)
	character.draw(screen)
	#screen.blit(bulletLayer, (0, 0))
	pygame.display.update()

	# bulletLayer is removed by MRP
	
	# update all stuff
	for c in character:
		c.update(movement)
		if frame % 10 == 0:
			playerProj.add(c.fire())
		# if check collide
		# if collide return index else return -1
		isHit = pygame.sprite.spritecollide(c, npcProj, True)
		if len(isHit) != 0:
			print("You Die")
			print("score :", takeDown)
			pygame.quit()

	for i in npc:
		isHit = pygame.sprite.spritecollide(i, playerProj, True)
		if len(isHit) != 0:
			if type(i).__name__ == "boss":
				bossCount -= 1
			i.kill()
			takeDown += 1
			continue
		i.update()
		if type(i).__name__ == "boss":
			npcProj.add(i.fire())
			continue

		if frame % 60 == 0:
			for c in character:
				npcProj.add(i.fire(c.getPos()))

	for b in npcProj:
		b.update()
		if b.isEnd():
			b.kill()

	for b in playerProj:
		b.update()
		if b.isEnd():
			b.kill()

	movement = pygame.math.Vector2(0, 0)

	# keep track current fps
	frame += 1
	frame %= 60
# bye bye
print(takeDown)
pygame.quit()
