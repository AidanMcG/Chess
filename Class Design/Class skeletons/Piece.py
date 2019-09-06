from abc import ABC, abstractmethod
from Board import Board

class Piece(ABC):
    
    def __init__(self, colour, coordinate, name)
        self.name = name
        self.colour = colour
        self.coordinate = coordinate
    
    @abstractmethod    
    def getPossibleMoves(self,x,y,board):
        pass
    
    def isInBounds(self,x,y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False
        
    def isConflict(self, x, y, board, CurrentColour ):
        if self.isInBounds(x,y) and ( """tile(x,y) == None or tile(x,y).Colour != CurrentColour"""):
            return True
        return False
        
    