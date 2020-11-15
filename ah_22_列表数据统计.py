name_list = ["zubay", "dinara", "zulnar", "zulay", "aypari", "UNSC", "UNSC", "UNSC", "UNSC", "UNSC", "UNSC", "UNSC",
             "UNSC", "UNSC"]
# len()可以统计变量的长度
# len(列表)可以统计列表的索引数
print("列表中有%d个索引" % len(name_list))
# name_list.count(欲统计的字符) 可以统计某一个数据出现的次数
print("列表中出现了%d次" % name_list.count("UNSC"))
# 小联系如何删除列表的全部某一个值
while not name_list.count("UNSC") == 0:
    name_list.remove("UNSC")
print(name_list)
print("删除完成")
