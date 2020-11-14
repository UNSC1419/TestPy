def say_hello():
    """打招呼"""
    print("你好啊！")


# say_hello()


def sum_2_num(num1, num2):
    """两个数字求和函数,参数1（int），参数2（int）"""
    result = num1 + num2
    return result


# print(sum_2_num(1, 2))


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


打印横线("!", 10, 5)
