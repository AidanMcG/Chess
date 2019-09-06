
class ChessTime:
	def __init__(self, whiteTime=300, blackTime=300):
		self.whiteTime = whiteTime
		self.blackTime = blackTime

	def getTime(self, colour):
		if colour == 'white':
			return self.whiteTime
		else:
			return self.blackTime

	def setTime(self, time):
		self.whiteTime = time
		self.blackTime = time

