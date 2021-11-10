from Node import Node
def board_print(board, base=3, side=9):
    # Stolen from https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
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
    def validate_block(block):
        used_nrs = set()
        for row in block:
            for col in row:
                if col.value == 0:
                    continue
                if col.value in used_nrs:
                    return False
                
                used_nrs.add(col.value)

        return True

    for row in range(0,3):
        for col in range(0,3):
            block = board[row*3 : (row+1) * 3]
            block[0] = block[0][col*3 : (col+1) * 3]
            block[1] = block[1][col*3 : (col+1) * 3]
            block[2] = block[2][col*3 : (col+1) * 3]
            if not validate_block(block):
                return False

    
    return True

def idx_to_pos(i):
    x = i // 9
    y = i % 9
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


import pygame
# Pygame code taken from: https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/

pygame.font.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")

# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)


font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

dif = 500 / 9 
# Function to draw required lines for making Sudoku grid        
def draw(grid):
    # Draw the lines
        
    for i in range (9):
        for j in range (9):
            if grid[i][j].value!= 0:
                # Fill blue color in already numbered grid
                if grid[i][j].known_value:
                    pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j].value), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and verticallyto form grid          
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)    

def solve(board):
    i = 0
    while True: 
        screen.fill((255, 255, 255))
        draw(board)
        pygame.display.update()
        pygame.time.wait(1)

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














