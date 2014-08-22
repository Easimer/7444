#7444
#Core
import pygame
from pygame.locals import *
from material import MatSys
from logger import Log
from core import Engine
from entity_sys import EntitySystem as EntSys
from physics import Physics

if __name__ == "__main__":
	Engine.Init()
	while Engine.properties["running"]:
		Engine.Event()
		Engine.KeyInput()
		Physics.GetSpace().step(0.02)
		EntSys.Think(0, Engine) #TODO: dt
		Engine.PreDraw()
		EntSys.Draw(Engine)
		Engine.PostDraw()
	Log.Message("Shutting down")
	EntSys.ClearEntities()
	MatSys.RemoveAllMaterial()
