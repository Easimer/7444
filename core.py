#7444
#Core

import pygame
import time
from pygame.locals import *
from material import MatSys
from logger import Log
from events import *
from entity_sys import EntitySystem as EntSys
from player import Player
from ground import Ground
from vector2d import Vector2D
from camera import Camera
from background import Background
from keys import KeysGuide
from sfxsys import SfxSys
from hud import HUD
from enemy import Enemy
from menu import Menu

import json
import io
import os.path
import random

class Engine:
	properties = {
		"screen" : (800, 600),
		"display" : (800,600),
		"title" : "7444",
		"state" : "STATE_LOADING",
		"entsys" : EntSys,
		"matsys" : MatSys,
		"keydown" : None,
		"camera" : None,
		"lastframe" : 0,
		"mousepos": (0, 0),
		"mousedown": (False, False, False),
		"score" : 0,
		"max_health" : 1000,
		"health" : 0,
		"energy" : 1000,
		"updatet" : 0,
		"e_health" : 100,
		"e_shoot" : True,
		"spawn_chance" : 0.02,
		"energy_regen" : 2.2,
		"torpedo_cost" : 10
	}

	@staticmethod
	def Init():
		Log.Message("Engine init")
		try:
			config = json.loads(open(os.path.join(os.path.dirname(__file__), "game.cfg"), "r").read())
			Engine.properties["screen"] = (config["resolution"][0], config["resolution"][1])
			Engine.properties["title"] = config["title"]
			Engine.properties["max_health"] = config["gameplay"]["player_health"]
			Engine.properties["energy"] = config["gameplay"]["player_energy"]
			Engine.properties["e_health"] = config["gameplay"]["enemy_health"]
			Engine.properties["e_shoot"] = config["gameplay"]["enemy_shoot_torpedo"]
			Engine.properties["energy_regen"] = config["gameplay"]["player_energy_regen"]
			Engine.properties["torpedo_cost"] = config["gameplay"]["torpedo_cost"]
		except IOError:
			Log.Warning("Config file not found or corrupted")
		Engine.properties["health"] = Engine.properties["max_health"]
		pygame.init()
		Engine.properties["lastframe"] = time.time()
		if not pygame.font: Log.Warning("Warning, font disabled")
		if not pygame.mixer: Log.Warning("Warning, sound disabled")
		Engine.properties["display"] = Engine.CreateWindow(Engine.properties["screen"])
		Engine.DisplayVideoInfo()
		Engine.SetCaption(Engine.properties["title"])
		MatSys.Init()
		Engine.LoadSounds()
		Engine.properties["font"] = pygame.font.Font("data/fonts/newscycle-regular.ttf", 18)
		SfxSys.Play(random.choice(["data/sfx/the_final_frontier.wav", "data/sfx/interstellar_survival_guide.wav"]) , True)
		Menu.Init(Engine)
		Engine.properties["state"] = "STATE_MENU"


	@staticmethod 
	def StartGame():
		Engine.properties["state"] = "STATE_RUNNING"
		HUD.Init(Engine)
		#Add required entities
		EntSys.AddEntity(Player, "player", Vector2D(200,200))
		EntSys.AddEntity(Camera, "camera")
		EntSys.AddEntity(Background, "background", Vector2D(-480,-270))
		KeysGuide.Load()
		Log.Message("Entering loop")
		

	@staticmethod
	def LoadSounds():
		SfxSys.LoadSound("data/sfx/torpedo.wav")
		SfxSys.LoadSound("data/sfx/the_final_frontier.wav")
		SfxSys.LoadSound("data/sfx/interstellar_survival_guide.wav")

	@staticmethod
	def AddPoints(p):
		Engine.properties["score"] += p

	@staticmethod
	def Shutdown():
		MatSys.Shutdown()
		pygame.quit()

	@staticmethod
	def GameplayUpdate():
		if Engine.properties["energy"] < 1000: #ship energy regen
			Engine.properties["energy"] += Engine.properties["energy_regen"]
	@staticmethod 
	def WriteText(text):
		return Engine.properties["font"].render(text, True, (255,255,255))
	@staticmethod
	def GetTS(t):
		if time.time() - Engine.properties["lastframe"] >= t:
			Engine.properties["lastframe"] = time.time()
			return True

	@staticmethod
	def SetCaption(caption):
		pygame.display.set_caption(caption)

	@staticmethod
	def CreateWindow(resolution):
		Engine.screen = pygame.display.set_mode(resolution, pygame.DOUBLEBUF)
		Engine.surface = pygame.display.get_surface()

	@staticmethod
	def Event():
		for event in pygame.event.get():
			PyGame_Events[event.type](event, Engine)

	@staticmethod
	def DisplayVideoInfo():
		vi = pygame.display.Info()
		Log.Message("Hardware Acceleration: " + ("yes" if vi.hw else "no (TODO)"))
		Log.Message(("Video Memory: " + (str(vi.wm) + "Mb" if vi.wm else "unknown")) if vi.hw else "")
		Log.Message("Width: " + str(vi.current_w) + " Height: " + str(vi.current_h))

	@staticmethod
	def PreDraw():
		Engine.screen.fill((3,25,36))

	@staticmethod
	def DrawImage(surface, position):
		rect = surface.get_rect()
		Engine.screen.blit(surface, pygame.Rect(position.x, position.y, surface.get_width(), surface.get_height()))

	@staticmethod
	def PostDraw(menu = False):
		if not menu:
			KeysGuide.DrawGuide(Engine)
			HUD.Draw(Engine)
		pygame.display.flip()
		pygame.display.update()

	@staticmethod
	def AddTestEntity():
		EntSys.AddEntity(TestEntity(),Engine)

	@staticmethod
	def KeyInput():
		Engine.properties["keydown"] = pygame.key.get_pressed()
		pass

	@staticmethod
	def MouseInput():
		Engine.properties["mousedown"] = pygame.mouse.get_pressed()
		Engine.properties["mousepos"] = pygame.mouse.get_pos()

	@staticmethod
	def update(a,s):
		pass

	@staticmethod
	def RandomEnemy(chance):
		if random.random() < chance:
			enemy = EntSys.AddEntity(Enemy, engine = Engine)
			enemy.set_pos(Vector2D(random.randint(Engine.properties["screen"][0]/2, Engine.properties["screen"][0]), random.randint(0, Engine.properties["screen"][1])))

	@staticmethod
	def HurtPlayer(hp):
		Engine.properties["health"] -= hp