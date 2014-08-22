#7444
#Physics

import pymunk

class Physics:
	properties = {
		"space" : None
	}

	@staticmethod
	def GetSpace():
		return Physics.properties["space"]

	@staticmethod
	def Init():
		Physics.properties["space"] = pymunk.Space()

	@staticmethod
	def CreateBody(mass, moment, position):
		body = pymunk.Body(mass, moment)
		body.position = position.x, position.y
		return body

	@staticmethod
	def CreateBox(body):
		return pymunk.Poly.create_box(body)

	@staticmethod
	def AddToSpace(body, poly):
		Physics.GetSpace().add(body, poly)