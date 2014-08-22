from entity_sys import EntitySystem
from entity import base_entity
from material import MatSys
from vector2d import Vector2D

from pygame.locals import *

class Player(base_entity):
	texture = "data/player.tga"

	def update(self,dt, engine):
		keys = engine.properties["keydown"]
		if keys:
			if keys[K_w]:
				self.position += Vector2D(0,-0.1)
			if keys[K_s]:
				self.position += Vector2D(0,0.1)
			if keys[K_a]:
				self.position += Vector2D(-0.1,0)
			if keys[K_d]:
				self.position += Vector2D(0.1,0)