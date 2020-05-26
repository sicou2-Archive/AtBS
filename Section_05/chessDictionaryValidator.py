row = range(8, 0, -1)
board = {}
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['8', '7', '6', '5', '4', '3', '2', '1']
board_valid = 1

def create_board():

    for i in column:
        for j in row:
            key = i + j
            board[key] = '[          ]'
    return board

def print_board(board):
    if board_valid == 0:
        print("This board is not valid.")
    elif board_valid == 1:
        for j in row:
            for i in column:
                square = i + j
                print(board[square], end='')
            print()
    else:
        print("You should not be here. Please go find an adult.")


def assign_pieces(pieces):
    for piece, position in pieces.items():
        if position == '':
            print("captured", piece)
        elif position not in board:
            print("Location error", piece)
            global board_valid
            board_valid = 0
        elif position:
            board[position] = piece
        else:
            print("You should not be here. Please go find an adult.")


pieces = {
    'max_pieces': 16,
    'max_king': 1,
    'max_queen': 1,
    'max_bishop': 2,
    'max_knight': 2,
    'max_rook': 2,
    'max_pawn': 8,
    }
w_pieces = {
    '[  w_king  ]': 'd1', '[  w_queen ]': 'e1', #h1
    '[w_k_bishop]': 'c1', '[w_q_bishop]': 'f1',
    '[w_k_knight]': 'b1', '[w_q_knight]': 'g1',
    '[ w_k_rook ]': 'a1', '[ w_q_rook ]': 'h1',
    '[ w_k_pawn ]': '',   '[ w_q_pawn ]': '',
    '[ w_kb_pawn]': '',   '[ w_qb_pawn]': '',
    '[ w_kk_pawn]': '',   '[ w_qk_pawn]': '',
    '[ w_kr_pawn]': '',   '[ w_qr_pawn]': '',
    }

b_pieces = {
    '[  b_king  ]': 'd8', '[  b_queen ]': 'e8',
    '[b_k_bishop]': 'c8', '[b_q_bishop]': 'f8',
    '[b_k_knight]': 'b8', '[b_q_knight]': 'g8',
    '[ b_k_rook ]': 'a8', '[ b_q_rook ]': 'h8',
    '[ b_k_pawn ]': 'd7', '[ b_q_pawn ]': 'e7',
    '[ b_kb_pawn]': 'c7', '[ b_qb_pawn]': 'f7',
    '[ b_kk_pawn]': 'b7', '[ b_qk_pawn]': 'g7',
    '[ b_kr_pawn]': 'a7', '[ b_qr_pawn]': 'h7',
    }

board = create_board()
assign_pieces(w_pieces)
assign_pieces(b_pieces)
print_board(board)