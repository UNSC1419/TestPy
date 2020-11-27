temp_str = "hello 123123123 world"
# 1. 判断是否以指定的字符串开始
print(temp_str.startswith("hello"))

# 2. 判断是否以指定的字符串结束
print(temp_str.endswith("world"))

# 3. 查找指定字符串，返回该字符串的索引位置,不存在则返回-1
# index同样可以查找，但是不存在会报错
print(temp_str.find("llo"))
print(temp_str.find("ABC"))
# 通过参数来指定查找范围0开始到整个字符串长度间
print(temp_str.find("world", 0, len(temp_str)))

# rfind 从右侧开始查找
print(temp_str.rfind("llo"))

# index 和find一样但是找不到会报错 0开始到整个字符串长度间
print(temp_str.index("world", 0, len(temp_str)))

# rindex 和rfind一样 找不到会报错
print(temp_str.rindex("world", 0, len(temp_str)))

# 4. 替换字符串,记得更新变量，replace执行会返回新字符串，但不会修改原来的变量
print(temp_str.replace("world", "世界"))
print(temp_str)
temp_str = temp_str.replace("world", "世界")
print(temp_str)
