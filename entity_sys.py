#7444
#Entity System

from logger import Log

class EntitySystem:
	entities = {}

	@staticmethod
	def AddEntity(entity, name = None,engine = None):
		Log.Message("Spawning entity " + str(entity) + " with name " + str(name if name else "<noname>"))
		EntitySystem.entities[name if name else (len(EntitySystem.entities) + 1)] = entity

	@staticmethod
	def Think(dt, engine):
		for ent in EntitySystem.entities:
				EntitySystem.entities[ent].update(dt, engine)

	@staticmethod
	def Draw(engine):
		for ent in EntitySystem.entities:
			if not ent == "player":
				EntitySystem.entities[ent].draw(engine)
		EntitySystem.entities["player"].draw(engine)

	@staticmethod
	def ClearEntities(engine = None):
		EntitySystem.entities = {}

	@staticmethod
	def EntityByName(name):
		return EntitySystem.entities[name] if EntitySystem.entities[name] else None