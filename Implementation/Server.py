from Client import Client
from ChessTime import ChessTime
from Board import Board

class Server:
    
	def __init__(self, turn="white"):
		self.turn = "white"
    
	def startGame(self, board):
		return board.getStartingBoard()
        
	def getTurn(self):
		return self.turn
    
	def updateBoard(self, board):		
		return board.updateBoard()    		   
    
	def isCheck():
		#if king can be taken
		#else not in check
		return
    
	def isCheckmate(self, king):
		#return Boolean for king being in checkmate
		current = self.getTurn()
		return current.king.getPossibleMoves == []
	    
	def getWinner(self):
		current = self.getTurn()
		if current == "white":
			opponent = "black"
		else:
			opponent = "white"

		#if current turn has no time, winner = other client
		if current.checkTime() == 0:
			return opponent

		#elif current player is in checkmate, winner = other client
    	elif current.isCheckmate():
			return opponent			

	def terminate():
		sys.exit()

	def getMoves():
		pass##########################

	def checkTime():
		current = self.getTurn()
		return current.getTime()
		
    

