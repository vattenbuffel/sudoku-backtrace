from Node import Node
from sudoku_generator import generate_sudoko
from back_trace import validate_board, solve, board_print


def numpy_to_list(np_board):
    board = []
    for y, np_row in enumerate(np_board):
        row = []
        for x, np_col in enumerate(np_row):
            row.append(Node(x, y, None if np_col == 0 else np_col))
        board.append(row)
    return board
        
np_board = generate_sudoko("extreme")
board = numpy_to_list(np_board)
print("Start board:")
board_print(board)

if not validate_board(board):
    raise ValueError("Unsolaveable board")

solve(board)
print("Solved board:")
board_print(board)
