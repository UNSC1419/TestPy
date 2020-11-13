# 这是第一种
# i = 1
# while i <= 5:
#     print("*"* i)
#     i += 1

# 这是第二种写法
# 初始化变量
row = 1
col = 1
# 循环当row小于等于10时结束
while row <= 10:
    # 嵌套一个循环当col小于等于row时结束
    while col <= row:
        # 打印*，扩展参数不换行
        print("*", end="")
        # col计数器+1
        col += 1
    # 打印换行
    print("")
    # 重置col计数器
    col = 1
    # row计数器+1
    row += 1 