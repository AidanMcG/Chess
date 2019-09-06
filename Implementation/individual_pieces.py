from pieces import Piece
from board import Board

class Bishop(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self,colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
        
    def bishopMoves(self, board):
        x = self.coordinate[0]
        y = self.coordinate[1]
        moves = []
        for i in range(1,16):
            if board.board.get((x+i,y+i)) is not None:
                moves.append((x+i,y+i))
                break
            moves.append((x+i,y+i))
        for i in range(1,16):
            if board.board.get((x-i,y+i)) is not None:
                moves.append((x-i,y+i))
                break
            moves.append((x-i,y+i))
        for i in range(1,16):
            if board.board.get((x+i,y-i)) is not None:
                moves.append((x+i,y-i))
                break
            moves.append((x+i,y-i))
        for i in range(1,16):
            if board.board.get((x-i,y-i)) is not None:
                moves.append((x-i,y-i))
                break
            moves.append((x-i,y-i))    
        return moves
        
    def getPossibleMoves(self, board):
        colour = self.colour
        return [(x,y) for x,y in self.bishopMoves(board) if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]

class Castle(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self,colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
        
    def castleMoves(self, board):
        x = self.coordinate[0]
        y = self.coordinate[1]
        moves = []
        for i in range(1,16):
            if board.board.get((x,y-i)) is not None:
                moves.append((x,y-i))
                break
            moves.append((x,y-i))
        for i in range(1,16):
            if board.board.get((x-i,y)) is not None:
                moves.append((x-i,y))
                break
            moves.append((x-i,y))    
        for i in range(1,16):
            if board.board.get((x+i,y)) is not None:
                moves.append((x+i,y))
                break
            moves.append((x+i,y))    
        for i in range(1,16):
            if board.board.get((x,y+i)) is not None:
                moves.append((x,y+i))
                break
            moves.append((x,y+i))  
        return moves
        
    def getPossibleMoves(self, board):
        colour = self.colour
        return [(x,y) for x,y in self.castleMoves(board) if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]
    
class Knight(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self,colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
        
    def knightMoves(self):
        x = self.coordinate[0]
        y = self.coordinate[1]
        return [(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2),(x+2,y+1),(x-2,y+1),(x+2,y-1),(x-2,y-1)]
        
    def getPossibleMoves(self, board):
        colour = self.colour
        return [(x,y) for x,y in self.knightMoves() if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]
    
class King(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self, colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
    
    def kingMoves(self):
        x = self.coordinate[0]
        y = self.coordinate[1]
        return [(x+1,y),(x,y+1),(x+1,y+1),(x-1,y),(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1)]
        
    def getPossibleMoves(self, board):
        colour = self.colour
        return [(x,y) for x,y in self.kingMoves() if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]
    
class Pawn(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self,colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
        
    def pawnMoves(self,board):
        x = self.coordinate[0]
        y = self.coordinate[1]
        moves = []
        if self.colour == "white":
            if board.board.get(x,y+2) is None:
                moves.append((x,y+2))
                if y == 2  and board.board.get((x,6))is None:
                    moves.append((x,4))
            if board.board.get((x+1,y+1)) is not None:
                moves.append((x+1,y+1))
            if board.board.get((x-1,y+1)) is not None:
                moves.append((x-1,y+1))
                
        if self.colour == "black":
            if board.board.get(x,y-2) is None:
                moves.append((x,y-2))
                if y == 15  and board.board.get((x,11))is None:
                    moves.append((x,11))
            if board.board.get((x+1,y-1)) is not None:
                moves.append((x+1,y-1))
            if board.board.get((x-1,y-1)) is not None:
                moves.append((x-1,y-1))
        return moves
        
        
    def getPossibleMoves(self,board):
        colour = self.colour
        moves = self.pawnMoves(board)
        return  [(x,y) for x,y in moves if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]
    
class Queen(Piece):
    def __init__(self, colour, coordinate, name):
        Piece.__init__(self,colour, coordinate, name)
        self.x = coordinate[0]
        self.y = coordinate[1]
        
    def queenMoves(self, board):
        x = self.coordinate[0]
        y = self.coordinate[1]
        moves = []
        for i in range(1,16):
            if board.board.get((x+i,y+i)) is not None:
                moves.append((x+i,y+i))
                break
            moves.append((x+i,y+i))
        for i in range(1,16):
            if board.board.get((x-i,y+i)) is not None:
                moves.append((x-i,y+i))
                break
            moves.append((x-i,y+i))
        for i in range(1,16):
            if board.board.get((x+i,y-i)) is not None:
                moves.append((x+i,y-i))
                break
            moves.append((x+i,y-i))
        for i in range(1,16):
            if board.board.get((x-i,y-i)) is not None:
                moves.append((x-i,y-i))
                break
            moves.append((x-i,y-i))    
        for i in range(1,16):
            if board.board.get((x,y-i)) is not None:
                moves.append((x,y-i))
                break
            moves.append((x,y-i))
        for i in range(1,16):
            if board.board.get((x-i,y)) is not None:
                moves.append((x-i,y))
                break
            moves.append((x-i,y))    
        for i in range(1,16):
            if board.board.get((x+i,y)) is not None:
                moves.append((x+i,y))
                break
            moves.append((x+i,y))    
        for i in range(1,16):
            if board.board.get((x,y+i)) is not None:
                moves.append((x,y+i))
                break
            moves.append((x,y+i))  
        return moves
        
    def getPossibleMoves(self, board):
        colour = self.colour
        return [(x,y) for x,y in self.queenMoves(board) if not self.isConflict(x ,y ,board, colour) and self.isInBounds(x,y)]