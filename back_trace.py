from Node import Node
def board_print(board):
    # Stolen from https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
    base = 3 
    side = 9
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums   = [ [""]+[symbol[n.value] for n in row] for row in board ]
    print(line0)
    for r in range(1,side+1):
        print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
        print([line2,line3,line4][(r%side==0)+(r%base==0)])


def validate_board(board):
    def validate(board_):
        for row in board_:
            used_vals = set()
            for col in row: # Col is of type Node
                if not col.value == 0 and col.value in used_vals:
                    return False
                used_vals.add(col.value)
        return True


    # Validate rows
    if not validate(board):
        return False

    # Validate cols 
    if not validate(list(map(list, zip(*board)))):
        return False

    # Validate 3x3 blocks
    for row in range(0,3):
        for col in range(0,3):
            board_ = board[row*3 : (row+1) * 3]
            board_[0] = board_[0][col*3 : (col+1) * 3]
            board_[1] = board_[1][col*3 : (col+1) * 3]
            board_[2] = board_[2][col*3 : (col+1) * 3]
            if not validate(board_):
                return False
    
    return True

def idx_to_pos(i):
    x = i % 9
    y = i // 9
    return x, y

def update_i(i, board, up):
    while True:
        if i == 80:
            return i
        i = i + 1 if up else i - 1
        x, y = idx_to_pos(i)
        if not board[y][x].known_value:
            return i

def reset(i, board):
    x, y = idx_to_pos(i)
    board[y][x].reset()

    i = update_i(i, board, False)
    x, y = idx_to_pos(i)
    if not board[y][x].update_val():
        return reset(i, board)

    return i




def solve(board):
    i = 0
    while True:
        x, y = idx_to_pos(i)
        node:Node = board[y][x]

        # If node has no value yet
        if node.value == 0:
            node.update_val()

        # board_print(board)
        if not validate_board(board):
            res = node.update_val()
            if not res:
                if i == 0:
                    raise ValueError("Unsolvable board")
                i = reset(i, board)
                # board_print(board)
        if not validate_board(board):
            continue

        
        if i == 80:
            #DONE
            return
        
        i = update_i(i, board, True)














