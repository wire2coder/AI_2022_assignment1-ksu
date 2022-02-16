# tiles.py
# use this file, like this: import tiles

import sys

class TileGame:

    def __init__(self, sampleBoard):
        self.legalMoves = legalMoves3
        self.goal = "12345678_"
        # self.goal = "1238_4765" # for assignment 1, unsolvable!

        self.dim = 3
        # self.makeManhatten()

    def getMoves(self, board):
        empty = board.find('_')

        # returning a 'tuple'
        stuff22 = self.legalMoves[empty] # for debugging
        return empty, self.legalMoves[empty]


    def makeMove(self, board, empty_location, mov_location):
        lbrd = list(board)
        lbrd[empty_location],lbrd[mov_location] = lbrd[mov_location],lbrd[empty_location]
        return "".join(lbrd) # 'join' items back into a 'string'


    # what is /f ???
    def printBoard(self, board: str, mesg: str = "", sep: str = "\f") -> None:
        if sep:
            print(sep)
        if mesg:
            print(mesg)

        expand = ["%02s" % x for x in board] # putting 2 'empty spaces' in front of the item
        rows = [0] * self.dim  # [0]*3 >> [0,0,0] # making a list with 3 items
        # rows = [1,1,1]

        for i in range(self.dim): # self.dim = 3
            rows[i] = "".join( expand[self.dim * i:self.dim * (i + 1)] ) # 'list slicing'

        print("\n".join(rows))

## end 'class' Tiles



# what is /f ???
def printBoard(board: str, mesg: str = "", sep: str = "\f") -> None:
    dim = 3

    if sep:
        print(sep)
    if mesg:
        print(mesg)

    expand = ["%02s" % x for x in board] # putting 2 'empty spaces' in front of the item
    rows = [0] * dim  # [0]*3 >> [0,0,0] # making a list with 3 items
    # rows = [1,1,1]

    for i in range(dim): #dim = 3
        rows[i] = "".join( expand[dim * i:dim * (i + 1)] ) # 'list slicing'

    print("\n".join(rows))



legalMoves3 = (  # for a 3x3 board
    (1, 3),  # these can slide into square 0
    (0, 4, 2),  # these can slide into square 1
    (1, 5),  # these can slide into square 2
    (0, 4, 6),  # these can slide into square 3
    (1, 3, 5, 7),  # these can slide into square 4
    (2, 4, 8),  # these can slide into square 5
    (3, 7),  # these can slide into square 6
    (4, 6, 8),  # these can slide into square 7
    (5, 7))  # these can slide into square 8



def main_test():
    startBoard = "4321_5678" # just a string
    game1 = TileGame(startBoard) # making a new 'object' from 'class'
    stuff1 = game1.getMoves(startBoard)
    game1.printBoard(startBoard, 'At move zero')
    #game1.futureCost(startBoard)

    print('\n for ::debugging:: wait here for a sec please')