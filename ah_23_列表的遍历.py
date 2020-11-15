name_list = ["a", "b", "c", "d", "e", "f", "g", "a", "b", "c", "d", "e", "f", "g"]
# for 容器变量（用来存放遍历的内容） in 被遍历列表
# for会遍历列表内的每一个索引并传递给容器变量
for name in name_list:
    print(name)

# 写一个for删除列表内所有”a“
for name in name_list:
    if name == "a":
        name_list.remove("a")
print(name_list)
