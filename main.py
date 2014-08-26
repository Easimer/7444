#7444
#Core
import pygame
from pygame.locals import *
from material import MatSys
from logger import Log
from core import Engine
from entity_sys import EntitySystem as EntSys
from menu import Menu

Engine.Init()
while Engine.properties["state"] == "STATE_MENU":
	
	Engine.Event()
	Engine.KeyInput()
	Engine.MouseInput()
	Menu.Update(Engine)
	Engine.PreDraw()
	Menu.Draw(Engine)
	Engine.PostDraw(True)
while Engine.properties["state"] == "STATE_RUNNING":
	Engine.Event()
	Engine.KeyInput()
	Engine.MouseInput()
	Engine.GameplayUpdate()
	Engine.RandomEnemy(Engine.properties["spawn_chance"])
	EntSys.Think(0, Engine)
	Engine.PreDraw()
	EntSys.Draw(Engine)
	Engine.PostDraw()
Log.Message("Shutting down")
EntSys.ClearEntities()
MatSys.RemoveAllMaterial()