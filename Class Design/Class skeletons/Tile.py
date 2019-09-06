Class Tile(object):
    def __init__(self, xCoord, yCoord, chessPiece):
        self.x = xCoord
        self.y = yCoord
        self.piece = chessPiece
        
    def isEmpty(self):
        return self.piece == None
    
    def getPiece(self):
        return self.piece
        