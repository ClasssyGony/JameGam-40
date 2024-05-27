import pygame, sys, time, random
from subcode.data import *
from subcode.camera import CameraGroup
from subcode.player import Player
from subcode.enemy import Enemy

# Setup Game
pygame.init()
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Setup FPS/Delta Time
clock = pygame.time.Clock()
prevTime = time.time()

# Camera
camera_group = CameraGroup()

# Player
player = Player((400, 400),camera_group)

# Enemy
enemy = Enemy((100,100),camera_group)

if __name__ == "__main__":
	while True:
		# Fill Surface
		WIN.fill((255,255,255))

		

		""" Delta Time """
		newTime = time.time()
		dt = newTime - prevTime
		prevTime = newTime

		""" EVENT HANDLER """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		""" Player Logic """
		#player.update(WIN,dt)
		
		""" Camera Display """
		camera_group.update(player,dt)
		camera_group.custom_draw(player)

		""" UPDATE DISPLAY SURFACE """
		pygame.display.update()