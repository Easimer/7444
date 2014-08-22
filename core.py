#7444
#Core

import pygame
from pygame.locals import *
from material import MatSys
from logger import Log
from events import *
from entity_sys import EntitySystem as EntSys
from player import Player
from ground import Ground
from vector2d import Vector2D
from physics import Physics

class Engine:
	properties = {
		"screen" : (640, 480),
		"display" : Player,
		"title" : "7444",
		"running" : True,
		"entsys" : EntSys,
		"matsys" : MatSys,
		"keydown" : None,
		"camera" : None
	}
	screen = Player
	surface = Player

	@staticmethod
	def Init():
		Log.Message("Engine init")
		pygame.init()
		if not pygame.font: Log.Warning("Warning, font disabled")
		if not pygame.mixer: Log.Warning("Warning, sound disabled")
		Engine.properties["display"] = Engine.CreateWindow(Engine.properties["screen"])
		Engine.DisplayVideoInfo()
		Engine.SetCaption(Engine.properties["title"])
		MatSys.Init()
		Physics.Init()
		EntSys.AddEntity(Player(), "player")
		EntSys.AddEntity(Ground(), "platform1")
		EntSys.EntityByName("platform1").set_pos(Vector2D(200,200))
		Log.Message("Entering loop")
	@staticmethod
	def Shutdown():
		MatSys.Shutdown()
		pygame.quit()

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
		Engine.screen.fill((0,0,0))

	@staticmethod
	def DrawImage(surface, position):
		Engine.screen.blit(surface, \
			pygame.Rect((position.x, position.y), surface.get_size()))

	@staticmethod
	def PostDraw():
		pygame.display.flip()
		pygame.display.update()

	@staticmethod
	def AddTestEntity():
		EntSys.AddEntity(TestEntity(),Engine)

	@staticmethod
	def KeyInput():
		Engine.properties["keydown"] = pygame.key.get_pressed()

	@staticmethod
	def update(a,s):
		pass