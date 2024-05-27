import pygame
from subcode.data import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.pos = pos
		self.image = pygame.Surface((50,50))
		self.cirle = pygame.draw.circle(self.image,(50,50,150),(25,25),20)
		self.rect = self.image.get_rect(center = self.pos)

		self.player_speed = CAMERA_SPEED
		self.canMove = True

	def move(self, dt):
		if self.canMove != False:
			key = pygame.key.get_pressed()
			move = pygame.Vector2((0, 0))
			if key[pygame.K_w]: move += (0, -1)
			if key[pygame.K_a]: move += (-1, 0)
			if key[pygame.K_s]: move += (0, 1)
			if key[pygame.K_d]: move += (1, 0)
			if move.length() > 0: move.normalize_ip()
			self.pos += move * dt * FIXED_FPS * self.player_speed
			self.rect.center = self.pos


	def update(self, _ , dt):
		self.move(dt)