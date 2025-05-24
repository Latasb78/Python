# ChessDictionaryValidator.py
print("Name:Lata.S.B",
       "AUID:1AY24AI060",
       "Section:O")
def is_valid_chess_position(position):
    """Check if the board position key is valid, e.g., 'a1' to 'h8'"""
    if len(position) != 2:
        return False
    file, rank = position[0], position[1]
    return file in 'abcdefgh' and rank in '12345678'

def is_valid_piece(piece):
    """Check if the piece is valid"""
    valid_pieces = {'K', 'Q', 'R', 'B', 'N', 'P'}
    return len(piece) == 2 and piece[0] in {'w', 'b'} and piece[1] in valid_pieces

def validate_chess_board(board):
    """Validate the chess board dictionary"""
    if not isinstance(board, dict):
        return False, "Input is not a dictionary"

    white_pieces = 0
    black_pieces = 0
    white_kings = 0
    black_kings = 0

    for position, piece in board.items():
        if not is_valid_chess_position(position):
            return False, f"Invalid board position: {position}"
        if not is_valid_piece(piece):
            return False, f"Invalid chess piece: {piece}"
        if piece[0] == 'w':
            white_pieces += 1
            if piece[1] == 'K':
                white_kings += 1
        elif piece[0] == 'b':
            black_pieces += 1
            if piece[1] == 'K':
                black_kings += 1

    if white_kings != 1:
        return False, "There must be exactly one white king"
    if black_kings != 1:
        return False, "There must be exactly one black king"
    if white_pieces > 16:
        return False, "Too many white pieces"
    if black_pieces > 16:
        return False, "Too many black pieces"

    return True, "Chess board is valid"

# Example usage
if _name_ == "_main_":
    board = {
        "a1": "wR", "b1": "wN", "c1": "wB", "d1": "wQ",
        "e1": "wK", "f1": "wB", "g1": "wN", "h1": "wR",
        "a2": "wP", "b2": "wP", "c2": "wP", "d2": "wP",
        "e2": "wP", "f2": "wP", "g2": "wP", "h2": "wP",
        "a8": "bR", "b8": "bN", "c8": "bB", "d8": "bQ",
        "e8": "bK", "f8": "bB", "g8": "bN", "h8": "bR",
        "a7": "bP", "b7": "bP", "c7": "bP", "d7": "bP",
        "e7": "bP", "f7": "bP", "g7": "bP", "h7": "bP"
    }

    valid, message = validate_chess_board(board)
    print(message)