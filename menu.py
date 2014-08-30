from material import MatSys
from entity import base_entity
from vector2d import Vector2D
from background import Background	
from steamworks import *

class StartGameButton(base_entity):
	position = Vector2D(100, 100)
	texture = "data/start_game.png"
	hovertexture = "data/start_game_hover.png"

	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 2 - MatSys.GetMaterial(self.texture).get_width() / 2, engine.properties["screen"][1] / 2 - MatSys.GetMaterial(self.texture).get_height() / 2)

	def OnClick(self, engine):
		engine.StartGame()

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

	def OnHover(self, engine):
		self.texture = self.hovertexture

class Logo(base_entity):
	texture = "data/logo.png"
	position = Vector2D(0, 10)
	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 2 - MatSys.GetMaterial(self.texture).get_width() / 2, 10)
	def update(self, engine): pass

class UpgradesPanel(base_entity):
	texture = "data/upgrades/panel.png"
	position = Vector2D(0, 10)
	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 8 - MatSys.GetMaterial(self.texture).get_width() / 2, 100)
	def update(self, engine): pass

class SteamPanel(base_entity):
	texture = "data/steam_panel.png"
	position = Vector2D(0, 400)
	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] - MatSys.GetMaterial(self.texture).get_width() - 100 , 100)
	def update(self, engine): pass

class Menu:
	elements = {}

	@staticmethod 
	def Init(engine):
		Menu.elements["background"] = Background(engine)
		Menu.elements["btnStartGame"] = StartGameButton(engine)
		Menu.elements["logo"] = Logo(engine)
		Menu.elements["u_panel"] = UpgradesPanel(engine)
		Menu.elements["u_hp"] = BtnUpgradeHP(engine)
		#Menu.elements["steam_panel"] = SteamPanel(engine)

	@staticmethod
	def Update(engine):
		Menu.elements["background"].update(0, engine)
		for element in Menu.elements:
			if not element == "background":
				Menu.elements[element].update(engine)
		
	@staticmethod 
	def Draw(engine):
		for element in ["background", "btnStartGame", "logo", "u_panel", "u_hp"]:
			Menu.elements[element].draw(engine)
		engine.DrawImage(engine.WriteText("Money: $" + str(engine.properties["money"])), Vector2D(10,10))
		engine.DrawImage(engine.WriteText("HP: " + str(engine.properties["upgrades"]["hp_mp"]) + "x"), Vector2D(10,30))
		#engine.DrawImage(engine.WriteText(Steam.GetPlayerName()), Vector2D(engine.properties["screen"][0] - MatSys.GetMaterial(Menu.elements["steam_panel"].texture).get_width() - 75, 186))
		#for friend in range(0, 6):
		#	engine.DrawImage(engine.WriteText(Steam.GetFriendNameByIndex(friend)), Vector2D(engine.properties["screen"][0] - MatSys.GetMaterial(Menu.elements["steam_panel"].texture).get_width() - 75, 220 + (44 * friend + 1)))
		#	engine.DrawImage(engine.WriteText(Steam.GetFriendPersonaStateByIndex(friend) if not Steam.IsFriendInGameByIndex(friend) else "In-Game: " + str(Steam.GetFriendGameByIndex(friend))), Vector2D(engine.properties["screen"][0] - MatSys.GetMaterial(Menu.elements["steam_panel"].texture).get_width() - 75, 242 + (44 * friend + 1)))


class BtnUpgradeHP(base_entity):
	position = Vector2D(100, 100)
	texture = "data/upgrades/hp_up.png"
	hovertexture = "data/upgrades/hp_up.png"

	def __init__(self, engine, texture = None):
		self.position = Vector2D(engine.properties["screen"][0] / 8 - MatSys.GetMaterial(self.texture).get_width() / 2, 130)

	def OnClick(self, engine):
		if engine.properties["money"] >= 20:
			engine.properties["upgrades"]["hp_mp"] *= 1.5
			engine.properties["money"] -= 20
			print("hp up")

	def update(self, engine):
		mpos = engine.properties["mousepos"]
		mclick = engine.properties["mousedown"]
		self.texture = "data/upgrades/hp_up.png"
		smat = MatSys.GetMaterial(self.texture)
		if (not ((self.position.y + smat.get_height() < mpos[1]) or (self.position.y > mpos[1]) or (self.position.x > mpos[0]) or (self.position.x + smat.get_width() < mpos[0]))) and (mclick[0] or mclick[1] or mclick[2]):
			self.OnClick(engine)
		elif not ((self.position.y + smat.get_height() < mpos[1]) or (self.position.y > mpos[1]) or (self.position.x > mpos[0]) or (self.position.x + smat.get_width() < mpos[0])):
			self.OnHover(engine)
		pass

	def OnHover(self, engine):
		self.texture = self.hovertexture
