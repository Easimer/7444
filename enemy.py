from entity import base_entity
import random
from vector2d import Vector2D
from material import MatSys
from entity_sys import EntitySystem as EntSys
from logger import Log
import math
from torpedo import PhotonTorpedo

class Enemy(base_entity):
	textures = ["data/space_ship_enemy.png", "data/space_ship_cube.png", "data/fluid_ship.tga"]
	movec = 1000
	addvec = None
	health = 25

	def __init__(self, engine, texture = None):
		self.health = engine.properties["e_health"]

	def load(self, engine, position = Vector2D(0,0)):
		self.position = position
		self.texture = random.choice(self.textures)
		MatSys.AddMaterial(self.texture)

	def update(self, dt, engine):
		if self.health <= 0:
			Log.Warning("Entity dead")
			engine.AddPoints(1)
			EntSys.RemoveEntity(self.name)
		if self.movec >= 150:
			playerpos = EntSys.EntityByName("player").position
			playerAngle = math.atan2(playerpos.y - self.position.y, playerpos.x - self.position.x)
			self.addvec = Vector2D(random.randint(-1, 1), random.randint(-1,1)) + Vector2D(math.cos(playerAngle), math.sin(playerAngle))
			self.movec = 0
			if engine.properties["e_shoot"]:
				torpedo = EntSys.AddEntity(PhotonTorpedo)
				torpedo.shoot(self.position + Vector2D(-16.5, 0), Vector2D(math.cos(playerAngle), math.sin(playerAngle)), True)
		self.position += self.addvec
		self.movec += 1