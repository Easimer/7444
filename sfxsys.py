import pygame

class SfxSys:

	sounds = {}

	@staticmethod
	def LoadSound(filename):
		SfxSys.sounds[filename] = pygame.mixer.Sound(filename)

	@staticmethod
	def Play(filename, loop = False):
		SfxSys.sounds[filename].play(-1 if loop else 0)