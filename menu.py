from material import MatSys
from entity import base_entity
from vector2d import Vector2D
from background import Background

class Button(base_entity):
	def update(self, engine):
		mpos = engine.properties["mousepos"]
		mclick = engine.properties["mousedown"]
		self.texture = "data/start_game.png"
		smat = MatSys.GetMaterial(self.texture)
		if (not ((self.position.y + smat.get_height() < mpos[1]) or (self.position.y > mpos[1]) or (self.position.x > mpos[0]) or (self.position.x + smat.get_width() < mpos[0]))) and (mclick[0] or mclick[1] or mclick[2]):
			self.OnClick(engine)
		elif not ((self.position.y + smat.get_height() < mpos[1]) or (self.position.y > mpos[1]) or (self.position.x > mpos[0]) or (self.position.x + smat.get_width() < mpos[0])):
			self.OnHover(engine)
		pass

	def OnClick(self, engine):
		pass

	def OnHover(self, engine):
		self.texture = self.hovertexture

class StartGameButton(Button):
	position = Vector2D(100, 100)
	texture = "data/start_game.png"
	hovertexture = "data/start_game_hover.png"

	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 2 - MatSys.GetMaterial(self.texture).get_width() / 2, engine.properties["screen"][1] / 2 - MatSys.GetMaterial(self.texture).get_height() / 2)

	def OnClick(self, engine):
		engine.StartGame()

class Logo(base_entity):
	texture = "data/logo.png"
	position = Vector2D(0 ,10)
	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 2 - MatSys.GetMaterial(self.texture).get_width() / 2, 10)
	def update(self, engine): pass

class Menu:
	elements = {}

	@staticmethod 
	def Init(engine):
		Menu.elements["background"] = Background(engine)
		Menu.elements["btnStartGame"] = StartGameButton(engine)
		Menu.elements["logo"] = Logo(engine)

	@staticmethod
	def Update(engine):
		Menu.elements["background"].update(0, engine)
		for element in Menu.elements:
			if not element == "background":
				Menu.elements[element].update(engine)
		
	@staticmethod 
	def Draw(engine):
		Menu.elements["background"].draw(engine)
		for element in Menu.elements:
			if not element == "background":
				Menu.elements[element].draw(engine)