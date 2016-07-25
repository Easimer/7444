from core import Engine

class Log:
	suppressWar = False

	@staticmethod
	def Error(msg):
		#if Engine.properties["debug"]:
			print("[7444 ERR] " + msg)
			pass

	@staticmethod
	def FatalError(msg):
		#if Engine.properties["debug"]:
			print("[7444 FER] " + msg)
			raise Exception(msg)

	@staticmethod
	def Warning(msg):
		if Engine.properties["debug"]:
			if not Log.suppressWar: print("[7444 WAR] " + msg)
		pass

	@staticmethod
	def Message(msg):
		if Engine.properties["debug"]:
			print("[7444 MSG] " + msg)
		pass