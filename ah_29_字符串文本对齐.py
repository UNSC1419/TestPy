pom = ["登鹳雀楼",
       "王之涣",
       "白日依山尽",
       "黄河入海流",
       "欲穷千里目",
       "更上一层楼", ]
for p in pom:
    # 使用CENTER来居中，可以指定宽度和填充字符，指定填充负责\u3000是中文全角空格，不指定默认是英文空格
    print("|%s|" % p.center(10, "\u3000"))

for p in pom:
    # 使用ljust来向左对齐，可以指定宽度和填充字符，指定填充负责\u3000是中文全角空格，不指定默认是英文空格
    print("|%s|" % p.ljust(10, "\u3000"))

for p in pom:
    # 使用rjust来向左对齐，可以指定宽度和填充字符，指定填充负责\u3000是中文全角空格，不指定默认是英文空格
    print("|%s|" % p.rjust(10, "\u3000"))
    # 使用XXX.strip可以去掉字符串两边的空格，lstrip和rstrip可以去左右两边的
    temp = p.rjust(10, "\u3000")
    print(temp.strip())
