row = 1
col = 1
while row <= 9:
    while col <= row:
        print("%-2d * %-2d = %-2d" % (col, row, row * col), end=" ")
        col += 1
    print("")
    col = 1
    row += 1
