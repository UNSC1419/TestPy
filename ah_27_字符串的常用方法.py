#
# 所有IS开头的方法都是判断类型的方法
#
# .isspace() 如果列表中只包含空格（或者空白字符如/t /r /n）则返回True
temp_list = " "
print(temp_list.isspace())

# .isalnum() 如果列表至少有一个字符并且所有字符都是字母或数字则返回true（汉字也算）
temp_list = "你好啊"
print(temp_list.isalnum())

# .isalpha 如果列表至少有一个字符并且所有字符都是字母则返回true（汉字也算）
temp_list = "你好啊"
print(temp_list.isalpha())

# .isdecimal()如果列表质保函数字则返回TRUE
temp_list = "123456"
print(temp_list.isdecimal())

# .istitle()如果列表内英文字母是标题化的（单词首字母大写的）则返回TRUE
temp_list = "1Unsc1419"
print(temp_list.istitle())

temp_list = "1Unsc1419"
print(temp_list.istitle())

# .islower()如果列表中字符都是小写的则返回true
temp_list = "1unsc1419"
print(temp_list.islower())

# .islower()如果列表中字符都是大写的则返回true
temp_list = "1UNSC1419"
print(temp_list.isupper())
