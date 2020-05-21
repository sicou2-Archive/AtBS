



# ISSUE IS WITH ASSIGN PIECES NOT SEEING A POSITIONAL ERROR
def create_board():
    row = range(8, 0, -1)
    board = {}

    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row = ['8', '7', '6', '5', '4', '3', '2', '1']
    for i in column:
        for j in row:
            key = i + j
            board[key] = ['        ']
    return board

def flip_flag():
    pos_error_flag = 0
    pos_error = "BOARD NOT VALID"
    pos_error_flag = 1
    print(pos_error_flag, 'FLAG')


def print_board(board):
    if pos_error_flag == 0:
        print(pos_error)
    elif pos_error_flag == 1:
        for j in row:
            for i in column:
                square = i + j
                print(board[square], end='')
            print()
    else:
        print("FORGET THIS")


def assign_pieces(pieces):
    for piece, position in pieces.items():
        print(piece, position, pos_error_flag)
    flip_flag()
    print(pos_error_flag, 'wut')
 #       board.get('i1', flip_flag())
#        i = board.get(position)
#
#
 #       if position:
  #          board[position] = piece
   #     elif position == '':
    #        print("captured", piece)
     #   elif position not in board.keys:
      #      print("Location error", piece)
       # else:
        #    print("error", piece)


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
    '[  w_king  ]': 'd1', '[  w_queen ]': 'i1', #h1
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