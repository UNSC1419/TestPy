row = 1
col = 1
while row <= 9:
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="")
        print(" ", end="")
        col += 1
    print("")
    col = 1
    row += 1
