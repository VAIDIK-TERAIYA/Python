
ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY_SLOT = ' '
PLAYER_1 = 'X'
PLAYER_2 = 'O'

def create_board():
    return [[EMPTY_SLOT for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    print("\n")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('-' * (COLUMN_COUNT * 4 - 1))

def drop_piece(board, column, piece):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][column] == EMPTY_SLOT:
            board[row][column] = piece
            return row, column
    return -1, -1

def check_win(board, row, col, piece):
    return (check_direction(board, row, col, piece, 0, 1) or 
            check_direction(board, row, col, piece, 1, 0) or  
            check_direction(board, row, col, piece, 1, 1) or 
            check_direction(board, row, col, piece, 1, -1))   


def check_direction(board, row, col, piece, dx, dy):
    count = 1 
    for i in range(1, 4):
        r = row + i * dy
        c = col + i * dx
        if 0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT and board[r][c] == piece:
            count += 1
        else:
            break
    for i in range(1, 4):
        r = row - i * dy
        c = col - i * dx
        if 0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT and board[r][c] == piece:
            count += 1
        else:
            break
    return count >= 4

def play_game():
    board = create_board()
    current_player = PLAYER_1
    game_over = False

    while not game_over:
        print_board(board)
        try:
            column = int(input(f"Player {current_player}'s turn. Choose a column (0-6): "))
            if column < 0 or column >= COLUMN_COUNT:
                print("Invalid column. Please choose a number between 0 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid column number.")
            continue
 
        row, col = drop_piece(board, column, current_player)
        if row == -1: 
            print("Column is full. Try another one.")
            continue
     
        if check_win(board, row, col, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        else:
            current_player = PLAYER_1 if current_player == PLAYER_2 else PLAYER_2

if __name__ == "__main__":
    play_game()
