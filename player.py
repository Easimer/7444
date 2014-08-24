from entity_sys import EntitySystem
from entity import base_entity
from material import MatSys
from vector2d import Vector2D

from pygame.locals import *

from camera import Camera
import math

from torpedo import PhotonTorpedo

from sfxsys import SfxSys

from enemy import Enemy

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
		isclick = engine.properties["mousedown"][0]

		if engine.properties["mousedown"][2]:
			EntitySystem.AddEntity(Enemy)

		mousepos = engine.properties["mousepos"]
		if isclick:
			torpedo = EntitySystem.AddEntity(PhotonTorpedo)
			deltaY = mousepos[1] - (self.position + Vector2D(99,34)).y
			deltaX = mousepos[0] - (self.position + Vector2D(99,34)).x
			angle = math.atan2(deltaY, deltaX)# * 180 / math.pi
			torpedo.shoot(self.position + Vector2D(99,34), Vector2D(math.cos(angle), math.sin(angle)))
			SfxSys.Play("data/sfx/torpedo.wav")
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
			