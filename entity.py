#7444
#Base Entity

from entity_sys import EntitySystem
from material import MatSys
from vector2d import Vector2D

from pygame.locals import *

class base_entity:
	parent = None
	position = Vector2D(0, 0)
	texture = None

	def load(self, engine, isPhysical = False, position = Vector2D(0,0)): #load() - add assets to the material system
		self.position = position
		if self.texture:
			MatSys.AddMaterial(self.texture)
		if isPhysical:
			pass

	def update(self, dt, engine): #update(dt: time since last frame(integer)) - doing AI, etc.
		pass
		
	def draw(self, engine): #draw() - draw the entity
		if not self.texture == None:
			engine.DrawImage(MatSys.GetMaterial(self.texture), self.position)

	def set_pos(self, new_pos):
		self.position = new_pos