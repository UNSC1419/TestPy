row = 1
col = 1
while row <= 9:
    while col <= row:
        print("%d*%d=%d\t" % (col, row, row * col), end="")
        col += 1
    print("")
    col = 1
    row += 1
