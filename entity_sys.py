#7444
#Entity System

from logger import Log
from vector2d import Vector2D

class EntitySystem:
	entities = {}
	spawnqueue = {}
	draw_over = True
	name = None
	@staticmethod
	def AddEntity(entity, name = None, position = Vector2D(0,0), physics = False, engine = None):
		nname = None
		if EntitySystem.draw_over:
			nname = name if name else (len(EntitySystem.entities) + 1)
			Log.Message("Spawning entity " + str(entity) + " with name " + str(name if name else "<noname>"))
			ent = entity()
			ent.name = name
			ent.load(engine, position)
			ent.set_pos(position)
			EntitySystem.entities[nname] = ent
			return EntitySystem.EntityByName(nname)
		else:
			Log.Warning("Think or draw is not over, adding to queue")
			EntitySystem.spawnqueue[nname] = (entity, nname, position)


	@staticmethod
	def Think(dt, engine):
		try:
			for ent in EntitySystem.entities:
				EntitySystem.entities[ent].update(dt, engine)
		except RuntimeError:
			pass

	@staticmethod
	def Draw(engine):
		EntitySystem.draw_over = False
		#EntitySystem.entities["background"].draw(engine)
		try:
			for ent in EntitySystem.entities:
				if not ent == "player" or not ent == "background":
					EntitySystem.entities[ent].draw(engine)
		except RuntimeError:
			pass
		EntitySystem.entities["player"].draw(engine)
		EntitySystem.draw_over = True
		for ent in EntitySystem.spawnqueue:
			entity = EntitySystem.spawnqueue[nname]
			EntitySystem.AddEntity(entity[0], entity[1], entity[2])

	@staticmethod
	def ClearEntities(engine = None):
		EntitySystem.entities = {}

	@staticmethod
	def EntityByName(name):
		return EntitySystem.entities[name] if EntitySystem.entities[name] else None

	@staticmethod
	def RemoveEntity(name):
		EntitySystem.entities[name] = None

	"""@staticmethod
	def CollisionCheck():
		lastent = None
		for ent in EntitySystem.entities:
			if not lastent:
				lastent = EntitySystem.entities[ent]
			elif lastend:
				ax1,ay1,ax2,ay2,bx1,by1,bx2,by2 = 0,0,0,0,0,0,0,0
				ax1 = lastent.position.x
				ay1 = lastent.position.y
				if lastent.texture:"""
