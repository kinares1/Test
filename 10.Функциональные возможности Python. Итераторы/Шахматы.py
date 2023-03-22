def defended_pawns(pawns):
    defended = 0
    for pawn in pawns:
        row = int(pawn[1])
        col = ord(pawn[0])
        if chr(col - 1) + str(row - 1) in pawns or chr(col + 1) + str(row - 1) in pawns:
            defended += 1
    return defended

print(defended_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
