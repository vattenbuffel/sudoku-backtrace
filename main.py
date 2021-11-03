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
# import numpy as np
# np_board = np.array([
#  [0 ,2 ,0 ,0 ,3 ,0 ,7 ,8 ,9],
#  [5 ,3 ,6 ,9 ,0 ,7 ,0 ,0 ,0],
#  [7 ,0 ,9 ,0 ,0 ,4 ,0 ,0 ,6],
#  [2 ,6 ,0 ,0 ,0 ,0 ,1 ,5 ,3],
#  [1 ,5 ,3 ,4 ,0 ,0 ,0 ,9 ,0],
#  [0 ,0 ,7 ,3 ,5 ,0 ,2 ,6 ,0],
#  [6 ,0 ,5 ,8 ,0 ,0 ,3 ,1 ,2],
#  [9 ,7 ,8 ,2 ,0 ,3 ,6 ,0 ,0],
#  [0 ,1 ,0 ,0 ,4 ,6 ,9 ,0 ,8]])
board = numpy_to_list(np_board)
print("Start board:")
board_print(board)


if not validate_board(board):
    raise ValueError("Unsolaveable board")

solve(board)
print("Solved board:")
board_print(board)


aioetnoihan = 5