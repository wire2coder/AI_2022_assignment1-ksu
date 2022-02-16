#  tilesSearch.py
#
#  Search for sequence of moves to bring a randomized tile puzzle
#  into 'order'

from collections import _OrderedDictItemsView, deque
import sys, time
import queue as Q # must use Python 3 or above

import tiles # tiles.py
from tiles import TileGame # tiles.py



def depth_first_search(game:TileGame, board:str):

    print(f"Depth-Fist Search :::")
    visited = set() # for depth_first_search()
    closed = {} # new 'dictionary' for keeping track of the 'node' that we 'VISITED'

    origCost = 0 
    orig = (origCost, 0, board, None) # ('cost', number of moves, board, parent node)

    closed[orig] = True # 'visited path' 'prevent looping in the "tree" '
    expanded = 0
    solution = None

    stack = []
    stack.append(orig)


    while stack and not solution:

        parent = stack.pop()
        expanded = expanded + 1 # increment 'expanded' by 1
        (parCost, parMoves, parBoard, ancester) = parent # 'un-packing' values


        if expanded == 999: # 'expanded' too many 'nodes', no 'solution'
            print(f"Depth-Fist Search :::")
            raise Exception("\nNo solution, code: 999")


        print(f">>> parent board:")
        tiles.printBoard(parBoard) # for debugging

        empty, moves = game.getMoves(parBoard)

        for mov in moves:
            childBoard = game.makeMove(parBoard, empty, mov)
            print(f"child board:")
            tiles.printBoard(childBoard)

            if closed.get(childBoard): # prevent 'looping in tree'
                continue # run the 'for mov in moves' again

            closed[childBoard] = True
            childMoves = parMoves + 1

            childCost = 0 + childMoves

            child = (childCost, childMoves, childBoard, parent)
            stack.append(child)

            if childBoard == game.goal:
                solution = child


    if solution: # 'solution' has a VALUEs
        stack_length = len(stack)
        print(f"\nDepth-Fist Search :::")
        print("%s entries expanded. Stack still has %s" % ( expanded, stack_length) )

        # find the 'path' leading to this 'solution'
        path = []

        while solution: # 'while' 'solution' has VALUEs
            path.append(solution[0:3]) # drop the parent
            solution = solution[3] # to grandparent


        path.reverse()

        return path
    else:    
        return [] # return empty 'list'
        raise Exception("No solution")




def bfs_search(game:TileGame, board:str)->[str]:
    #def search(game:TileGame, board:TileGame, ratio:int)->"nothing":
    print(f"Breadth-Fist Search :::")

    closed = {} # new 'dictionary' for keeping track of the 'node' that we 'VISITED'

    from collections import deque
    #queue = Q.PriorityQueue() # 'Queue data structure'
    queue = deque()

    # origCost = game.futureCost(board) * ratio
    origCost = 0 # for 'breath first search'

    orig = (origCost, 0, board, None) # ('cost', number of moves, board, parent node)
    #queue.put(orig)
    queue.appendleft(orig)

    closed[orig] = True # 'visited path' 'prevent looping in the "tree" '
    expanded = 0
    solution = None


    # start searching loop
    while queue and not solution: # still have 'stuff' in the 'Queue' AND run loop until 'solution' has a VALUE
        #parent = queue.get() # get LAST item in the 'Queue (data structure) '
        parent = queue.pop() # get LAST item in the 'Queue (data structure) '
        expanded = expanded + 1 # increment 'expanded' by 1
        (parCost, parMoves, parBoard, ancester) = parent # 'un-packing' values

    
        print(f">>> parent board:")
        tiles.printBoard(parBoard) # for debugging
         # getting 'index location' of the 'blank tile'
         # getting the 'allowable moves'
        empty, moves = game.getMoves(parBoard)

        for mov in moves:
            childBoard = game.makeMove(parBoard, empty, mov)
            print(f"child board:")
            tiles.printBoard(childBoard)

            if closed.get(childBoard): # prevent 'looping in tree'
                continue # run the 'for mov in moves' again

            closed[childBoard] = True
            childMoves = parMoves + 1

            # childCost = game.futureCost(childBoard) * ratio + childMoves
            childCost = 0 + childMoves

            child = (childCost, childMoves, childBoard, parent)
            #queue.put(child)
            queue.appendleft(child)

            if childBoard == game.goal:
                solution = child

    if solution: # 'solution' has a VALUEs
        q_size = len(queue)
        print(f"\nBreadth-Fist Search :::")
        print("%s entries expanded. Queue still has %s" % ( expanded,   q_size ))

        # find the 'path' leading to this 'solution'
        path = []

        while solution: # 'while' 'solution' has VALUEs
            path.append(solution[0:3]) # drop the parent
            solution = solution[3] # to grandparent


        path.reverse()

        return path
    else:
        return [] # return empty 'list'
        raise Exception("No solution")


def main():


    import tilesScramble

    # get a 'shuffled puzzle board'
    # board1 = '1234687_5'
    board1 = tilesScramble.scramble(5) # i'm just making it 'shuffle' the puzzle 5 times

    timed = 1 # for timing the 'run time' of the program

    # game1: TileGame object, making new 'TileGame object'
    game1 = TileGame(board1)

    startTime = time.time() # start timing


    ### run the 'SEARCH algorithm'
    #############################

    #path = depth_first_search(game1, board1)
    path = bfs_search(game1, board1)
    


    elapsed = time.time() - startTime # stop timing

    if timed:
        timeMsg = "Search took %s secs" % round(elapsed, 4)
    else: timeMsg = ""

    print("tilesSearch.py: Moves=%s %s" % ( len(path), timeMsg) )

    for entry in path: # print out all the individual stuff in the 'path'
        print(entry)


if __name__ == '__main__':
    main()
    print('\n for ::debugging:: wait here for a sec please')



