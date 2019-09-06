from Pieces import Piece

class Bishop(Piece):
    def getPossibleMoves(self, x, y, board):
        colour = self.colour
        return 

class Castle(Piece):
    def getPossibleMoves(self, x, y, board):
    return
    
class Knight(Piece):
    def knightMoves(x, y):
        return [(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2),(x+2,y+1),(x-2,y+1),(x+2,y-1),(x-2,y-1)]
    def getPossibleMoves(self, x, y, board):
    return
    
class King(Piece):
    def kingMoves(x,y):
        return [(x+1,y),(x,y+1),(x+1,y+1),(x-1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
        
    def getPossibleMoves(self, x, y, board):
    colour = self.colour
    return [(x,y) for x,y in kingMoves(x,y) if not self.isConflict(x ,y ,board, colour)]
    
class Pawn(Piece):
    def getPossibleMoves(self, x, y, board):
    return
    
class Queen(Piece):
    def getPossibleMoves(self, x, y, board):
    return 