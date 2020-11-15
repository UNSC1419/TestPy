user1 = {"name": "unsc",
         "age": 18,
         "admin": True,
         "server": 192.168,
         }
print(user1)
# 1.字典取值
# 如果取值时键不存在会报错
print(user1["name"])
# 2.修改字典
user1["age"] = 20
print(user1["age"])
# 如果键不存在会创建这个键
user1["root"] = False
print(user1)
# 删除
user1.pop("root")
print(user1)

# 统计字典中键值对的数量
print(len(user1))

# 合并字典,如果被合并的字典中有相同的键，该键数据会被更新
temp = {1: "123",
        2: 456,
        3: 3.141592654579,
        "server": 172.16}
user1.update(temp)
print(user1)

# 清空字典
temp.clear()
print(temp)
# 也可使用del
del temp

# for 遍历字典
temp = {"user": "unsc",
        "qq": "1121145025",
        "phone": "13451235421"}
# 这里的K变量指字典中的键名（key）
# 通过for 遍历出K键名后使用temp[K（键名）]取出键值
for k in temp:
    print("%s - %s" % (k, temp[k]))
