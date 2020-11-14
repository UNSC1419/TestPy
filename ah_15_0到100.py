# 初始化变量
i = 0
h = 0
while i <=100:
    h+= i
    i+= 1
print("0到100的合为%d"%h)

# 初始化变量
i = 0
h = 0
# 求0到100的偶数合
while i <= 100:
    if not (i % 2):
        h += i
    i += 1
print("0-100偶数合为%d" % h)

# 初始化变量
i = 0
h = 0
# 求0到100的奇数合
while i <= 100:
    if (i % 2):
        h += i
    i += 1
print("0-100偶数合为%d" % h)
