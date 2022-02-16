# tilesScramble.py
# Scramble the 'solution board' by making 'N' random moves

def scramble(times):
    import tiles # tiles.py
    import random

    board = "12345678_"
    # tiles.py >> TileGame (class) >> __init__(self, input)
    game = tiles.TileGame(board)
    used = {} # dictionary
    while times > 0:
        used[board] = True # mark as taken
        empty, moves = game.getMoves(board)
        move = random.choice(moves)
        nextBoard = game.makeMove(board, empty, move)

        if used.get(nextBoard): # if used.get(nextBoard) == True
            continue

        board = nextBoard
        times = times - 1

    return board


def main():
    import sys, random
    import tiles # tiles.py
    # import sarg # sarg.py >> for 'parsing argument' when running from command line $python tilesScrable.py moves=21

    # moves = sarg.Int("moves", 20) # Number of times to randomly move, 'moves' is an INTEGER
    # print(scramble(moves))

    # my_board1 = "4321568_7"
    # gameo1 = tiles.TileGame(my_board1)
    # gameo1.dim
    # allow_moves = gameo1.getMoves(my_board1)

    for asdf in range(0, 4):
        random_int = random.randint(0, 9)
        what1 = scramble(random_int)
        tiles.printBoard(what1)

    print('\n for ::debugging:: wait here for a sec please')

if __name__ == "__main__":
    main()






