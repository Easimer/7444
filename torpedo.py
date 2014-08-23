from entity import base_entity
from entity_sys import EntitySystem as EntSys
from logger import Log
import math
from vector2d import Vector2D

class PhotonTorpedo(base_entity):
	texture="data/torpedo.tga"
	target = None
	def update(self, dt, engine):
		if self.target and not self.position == self.target:
			deltaY = self.target.y - self.position.y
			deltaX = self.target.x - self.position.x
			angle = math.atan2(deltaY, deltaX) * 180 / math.pi
			self.position += Vector2D(math.cos(angle) * 2, math.sin(angle) * 2)
		if self.position == self.target:
			EntSys.RemoveEntity(self.name)
	def shoot(self, start, target):
		Log.Message("Shooting torpedo from " + str(start) + " to " + str(target))
		self.position = start
		self.target = target