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
	health = 5000
	shield = False

	def __init__(self, engine, texture = None):
		self.health = 5000 * engine.properties["upgrades"]["hp_mp"]

	def load(self, engine, position = Vector2D(0,0)): #load() - add assets to the material system
		self.position = position
		MatSys.AddMaterial("data/space_ship.png")
		MatSys.AddMaterial("data/space_ship_right.png")
		MatSys.AddMaterial("data/space_ship_up.png")
		MatSys.AddMaterial("data/space_ship_down.png")

	def update(self, dt, engine):
		if self.health < 0:
			engine.properties["state"] = "STATE_MENU"
		EntitySystem.CollisionCheck(self, 25, False, True)
		keys = engine.properties["keydown"]	
		engine.properties["health"] = self.health
		mousepos = engine.properties["mousepos"]
		if engine.properties["mousedown"][0] and engine.properties["energy"] >= 10:
			torpedo = EntitySystem.AddEntity(PhotonTorpedo)
			deltaY = mousepos[1] - (self.position + Vector2D(5,5)).y
			deltaX = mousepos[0] - (self.position + Vector2D(5,5)).x
			angle = math.atan2(deltaY, deltaX)
			torpedo.shoot(self.position + Vector2D(5,5), Vector2D(math.cos(angle), math.sin(angle)))
			SfxSys.Play("data/sfx/torpedo.wav")
			engine.properties["energy"] -= engine.properties["torpedo_cost"]

		if engine.properties["mousedown"][2]:
			self.shield = True
			engine.properties["energy"] -= 3.0
		else:
			self.shield = False
		
		if keys:
			if keys[K_w]:
				self.position += Vector2D(0, -5) if self.position.y >= 5 else Vector2D(0,0)
				self.texture = "data/space_ship_up.png"
				EntitySystem.EntityByName("background").move(Vector2D(0,1)) if self.position.y >= 5 else Vector2D(0,0)
			if keys[K_s]:
				self.position += Vector2D(0, 5) if self.position.y <= engine.properties["screen"][1] - 70 else Vector2D(0,0)
				self.texture = "data/space_ship_down.png"
				EntitySystem.EntityByName("background").move(Vector2D(0,-1)) if self.position.y <= engine.properties["screen"][1] - 70 else Vector2D(0,0)
			if keys[K_a]:
				self.position += Vector2D(-5, 0) if self.position.x >= 10 else Vector2D(0,0)
				EntitySystem.EntityByName("background").move(Vector2D(1,0)) if self.position.x >= 10 else Vector2D(0,0)
			if keys[K_d]:
				self.position += Vector2D(5, 0) if self.position.x <= engine.properties["screen"][0] - 42 else Vector2D(0,0)
				self.texture = "data/space_ship_right.png"
				EntitySystem.EntityByName("background").move(Vector2D(-1,0)) if self.position.x <= engine.properties["screen"][0] - 42 else Vector2D(0,0)
			else:
				self.texture = "data/space_ship.png"
			

class Shield(base_entity):
	texture = "data/shield.png"
	dodraw = False
	def update(self, dt, engine): #update(dt: time since last frame(integer)) - doing AI, etc.
		self.position = EntitySystem.EntityByName("player").position
		if EntitySystem.EntityByName("player").shield:
			self.dodraw = True
		else:
			self.dodraw = False
		
	def draw(self, engine): #draw() - draw the entity
		if self.texture and self.dodraw:
			engine.DrawImage(MatSys.GetMaterial(self.texture), self.position)