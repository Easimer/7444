#7444
#Camera

from entity import base_entity
from entity_sys import EntitySystem as EntSys

class Camera(base_entity):
	CameraX = 0
	def update(self, dt, engine):
		CameraX = EntSys.EntityByName("player").position.x