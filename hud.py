import pygame
from vector2d import Vector2D

class HUD:
	hud_surface = None
	@staticmethod 
	def Init(engine):
		HUD.hud_surface = pygame.Surface(engine.properties["screen"], pygame.SRCALPHA, 32)
		HUD.hud_surface = HUD.hud_surface.convert_alpha()
	@staticmethod 
	def DrawHealth(engine):
		pygame.draw.rect(HUD.hud_surface, (255,0,0), pygame.Rect(10, HUD.hud_surface.get_height() - 20, engine.properties["health"] / 50, 10))

	@staticmethod 
	def DrawPower(engine):
		pygame.draw.rect(HUD.hud_surface, (252,215,0), pygame.Rect(10, HUD.hud_surface.get_height() - 40, engine.properties["energy"] / 10, 10))

	@staticmethod 
	def DrawScore(engine):
		HUD.hud_surface.blit(engine.WriteText("Score: " + str(engine.properties["score"])), (10, HUD.hud_surface.get_height() - 68))

	@staticmethod
	def Draw(engine):
		HUD.hud_surface.fill((0,0,0,0))
		HUD.DrawHealth(engine)
		HUD.DrawPower(engine)
		HUD.DrawScore(engine)
		engine.DrawImage(HUD.hud_surface, Vector2D(0,0))