from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, colour, coordinate, name):
        self.name = name
        self.colour = colour
        self.coordinate = coordinate
        self.x = coordinate[0]
        self.y = coordinate[1]
    
    @abstractmethod    
    def getPossibleMoves(self,x,y,board):
        pass
    
    def isInBounds(self,x,y):
        if x >= 1 and x < 9 and y >= 1 and y < 9:
            return True
        return False
        
    def isConflict(self, x, y, board, CurrentColour):
        return not( self.isInBounds(x,y) and (board.board.get((x,y)) == None or board.board.get((x,y)).colour != CurrentColour))