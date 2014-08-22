#7444
#Material System
import pygame
from logger import Log

class MatSys:

	materials = {} # path (str) : image (Surface)
	@staticmethod
	def AddMaterial(filepath):
		Log.Message("Loading material " + filepath)
		MatSys.materials[filepath] = pygame.image.load(filepath)
		Log.Message("Available materials: ")
		for k,v in MatSys.materials.items():
			print(k,v)
	
	@staticmethod
	def GetMaterial(filepath):
		try:
			return MatSys.materials[filepath]
		except KeyError:
			Log.Warning("Material " + filepath + " is not loaded")
			MatSys.AddMaterial(filepath)
			return MatSys.materials[filepath]

	@staticmethod
	def RemoveAllMaterial():
		MatSys.materials.clear()

	@staticmethod
	def Init():
		Log.Message("Material system started")

	@staticmethod
	def Shutdown():
		MatSys.RemoveAllMaterial()