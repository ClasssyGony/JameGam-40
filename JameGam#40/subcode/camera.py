import pygame, random

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		
		# camera offset 
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# Background
		self.background_surf = pygame.Surface((1500, 1500))
		self.background_surf.fill((30, 30, 30))
		self.background_rect = self.background_surf.get_rect(topleft = (0,0))

		for _ in range(3000):
			x, y = random.randint(0, 1000), random.randint(0, 1000)
			pygame.draw.rect(self.background_surf, pygame.Color('green'), (x, y, 2, 2))

		# box setup
		self.camera_borders = {'left': 300, 'right': 300, 'top': 300, 'bottom': 300}
		l = self.camera_borders['left']
		t = self.camera_borders['top']
		w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
		h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
		self.camera_rect = pygame.Rect(l,t,w,h)

	def box_target_camera(self,target):

		if target.rect.left < self.camera_rect.left:
			self.camera_rect.left = target.rect.left
		if target.rect.right > self.camera_rect.right:
			self.camera_rect.right = target.rect.right
		if target.rect.top < self.camera_rect.top:
			self.camera_rect.top = target.rect.top
		if target.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = target.rect.bottom

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']

	def custom_draw(self, player):
		self.box_target_camera(player)

		# background
		background_offset = self.background_rect.topleft - self.offset
		self.display_surface.blit(self.background_surf, background_offset)		

		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
