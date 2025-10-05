dictionary = {'1h': "bK", '6c': "wQ", '2g': "bB", '5h': "bQ", '3e': "wK"}


def is_valid_chess_board(dictionary):
    pieces = list(dictionary.values())
    cords = dictionary.keys()

    x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]
    y_axis = [1, 2, 3, 4, 5, 6, 7, 8]

    valid_cords = []
    for y_value in y_axis:
        for x_value in x_axis:
            valid_cords.append(str(y_value) + x_value)

    valid_piece_name = ["P", "N", "B", "R", "Q", "K"]

    if pieces.count('bK') == 1 and pieces.count('wK') == 1:
        all_tests_passed = True

        white_pieces = 0
        black_pieces = 0
        white_pawns = 0
        black_pawns = 0
        for piece in pieces:
            if piece.startswith("w"):
                white_pieces += 1
            elif piece.startswith("b"):
                black_pieces += 1
            if piece == "wP":
                white_pawns += 1
            elif piece == "bP":
                black_pawns += 1

        if not (white_pieces <= 16 and black_pieces <= 16):
            all_tests_passed = False

        if not (white_pawns <= 8 and black_pawns <= 8):
            all_tests_passed = False

        if all_tests_passed:
            for cord in cords:
                if cord not in valid_cords:
                    all_tests_passed = False
                    break

        if all_tests_passed:
            for piece in pieces:
                if not piece.startswith(('w', 'b')) or piece[1:] not in valid_piece_name:
                    all_tests_passed = False
                    break

        return all_tests_passed
    else:
        return False


result = is_valid_chess_board(dictionary)

print(result)
