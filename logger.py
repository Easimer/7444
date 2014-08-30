class Log:
	suppressWar = False

	@staticmethod
	def Error(msg):
		print("[7444 ERR] " + msg)
		pass

	@staticmethod
	def FatalError(msg):
		print("[7444 FER] " + msg)
		raise Exception(msg)

	@staticmethod
	def Warning(msg):
		if not Log.suppressWar: print("[7444 WAR] " + msg)
		pass

	@staticmethod
	def Message(msg):
		print("[7444 MSG] " + msg)
		pass