def safe_pawns(pawns):
    pawns = list(pawns)
    count = 0
    for i in pawns:
        ad1 = chr(ord(i[0])-1) + str(int(i[1])-1)
        ad2 = chr(ord(i[0])+1) + str(int(i[1])-1)
        if ad1 in pawns or ad2 in pawns:
            count += 1
    return count

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
