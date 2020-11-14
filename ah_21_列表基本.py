name_list = ["zubay", "dinara", "zulnar", "zulay", "aypari"]
# 1.取值
print(name_list[3])
# 2.取索引
print(name_list.index("dinara"))
# 3.修改
name_list[3] = "商岳"
print(name_list[3])
# 4.增加数据
# name_list.append()向列表最后添加数据
name_list.append("UNSC")
print(name_list)
# 5.插入数据
# name_list.insert(插入索引,插入的数据)
name_list.insert(4, "插入的数据")
print(name_list)
# 6.扩展数据
# 接收扩展的列表名.extend(扩展列表)
test_list = ["A", "B", "C"]
name_list.extend(test_list)
print(name_list)
# 7.删除
# name_list.remove("USNC") 可以删除该值第一次出现的索引
# 添加一个USNC进去，使列表里有两个USNC，使用remove删除USNC后，还剩下一个USNC
name_list.append("UNSC")
print(name_list)
name_list.remove("UNSC")
print(name_list)
# name_list.pop(弹栈位置)不写参数pop会弹出最后一个索引（删除并返回这个值）
print(name_list.pop(0))
print(name_list)
# name_list.clear()会直接清空列表
name_list.clear()
print(name_list)
# del 会直接删除从内存中变量
# del name_list[X]也可以删除列表中的单个索引
del name_list
