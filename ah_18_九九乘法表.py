# 初始化变量
row = 1
col = 1
# 行数循环
while row <= 9:
    #列数循环
    while col <= row:
        # 打印例子2*3=6（对齐制表符）,取消换行
        print("%d*%d=%d\t" % (col, row, row * col), end="")
        # 列计数器
        col += 1
    #打印换行
    print("")
    #初始化列计数器
    col = 1
    #行计数器
    row += 1
