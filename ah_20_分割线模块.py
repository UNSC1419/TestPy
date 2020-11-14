def 打印横线(字符, 列数, 行数):
    """打印多行分割线

    :param 字符:分割线使用的字符
    :param 列数:分割线的列数
    :param 行数:分割线的行数
    """
    row = 0
    while row < 行数:
        print(字符 * 列数)
        row += 1
    return


name = "分割线模块"
