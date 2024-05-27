import pygame, random
from subcode.data import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# Enemy Variables
		self.pos = pygame.math.Vector2(pos)
		self.direction = pygame.math.Vector2()
		self.state = ENEMY_STATES[0]

		# Setting Up Enemy Characteristic
		self.enemy_type = random.choice(ENEMY_TYPES)
		self.speed = ENEMY_SPEED[self.enemy_type]
		self.colour = ENEMY_COLOUR[self.enemy_type]

		# Surface & Rect
		self.image = pygame.surface.Surface((50,50))
		self.rect = self.image.get_rect(center = self.pos)

		self.image.fill(self.colour)

	def hunt_player(self, player, dt):
		""" Hunt the player down """

		if self.state == "Hunt":
			# Find Vector between the enemy and the player
			player_vector = pygame.math.Vector2(player.rect.center)
			enemy_vector = pygame.math.Vector2(self.rect.center)
			distance = (player_vector - enemy_vector).magnitude()

			if distance > 0:
				self.direction = (player_vector - enemy_vector).normalize()
			else:
				self.direction = pygame.math.Vector2()
			
			# Calculate Velocity
			self.velocity = self.direction * self.speed * dt * FIXED_FPS
			self.pos += self.velocity

			# Update Enemy Pos
			self.rect.centerx = self.pos.x
			self.rect.centery = self.pos.y

	def update(self, player, dt):
		self.hunt_player(player,dt)