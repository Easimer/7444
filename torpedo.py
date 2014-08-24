from entity import base_entity
from entity_sys import EntitySystem as EntSys
from logger import Log
import math
from vector2d import Vector2D

class PhotonTorpedo(base_entity):
	texture="data/torpedo.tga"
	target = None
	velocity = 0.5
	def update(self, dt, engine):
		if self.velocity < 100: #why not
			self.velocity *= 1.1
		else:
			#Log.Message("Torpedo is too fast, destroying")
			EntSys.RemoveEntity(self.name)
		self.position += self.target * self.velocity
	def shoot(self, start, target):
		#Log.Message("Shooting torpedo from " + str(start) + " to " + str(target))
		self.position = start
		self.target = target