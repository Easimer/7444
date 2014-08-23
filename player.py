from entity_sys import EntitySystem
from entity import base_entity
from material import MatSys
from vector2d import Vector2D

from pygame.locals import *

from camera import Camera
import math

from torpedo import PhotonTorpedo

class Player(base_entity):
	texture = "data/space_ship.png"
	rotation = 0
	lastrot = 0
	active = False
	def load(self, engine, position = Vector2D(0,0)): #load() - add assets to the material system
		self.position = position
		MatSys.AddMaterial("data/space_ship.png")
		MatSys.AddMaterial("data/space_ship_right.png")
		MatSys.AddMaterial("data/space_ship_up.png")
		MatSys.AddMaterial("data/space_ship_down.png")

	def update(self, dt, engine):
		keys = engine.properties["keydown"]
		mousepos = Vector2D(engine.properties["mousepos"])
		isclick = engine.properties["mousedown"][0]
		if isclick:
			torpedo = EntitySystem.AddEntity(PhotonTorpedo)
			torpedo.shoot(self.position + Vector2D(0,0.000000001), mousepos)
		if keys:
			if keys[K_w]:
				self.position += Vector2D(0, -5) if self.position.y >= 5 else Vector2D(0,0)
				self.texture = "data/space_ship_up.png"
				EntitySystem.EntityByName("background").move(Vector2D(0,1))
			if keys[K_s]:
				self.position += Vector2D(0, 5) if self.position.y <= engine.properties["screen"][1] - 70 else Vector2D(0,0)
				self.texture = "data/space_ship_down.png"
				EntitySystem.EntityByName("background").move(Vector2D(0,-1))
			if keys[K_a]:
				self.position += Vector2D(-5, 0)
				EntitySystem.EntityByName("background").move(Vector2D(1,0))
			if keys[K_d]:
				self.position += Vector2D(5, 0)
				self.texture = "data/space_ship_right.png"
				EntitySystem.EntityByName("background").move(Vector2D(-1,0))
			else:
				self.texture = "data/space_ship.png"
			