# 使用多个键值，储存对一个对象的相关信息，可以描述更复杂的数据信息
# 将多个字典放置在一个列表中，然后进行for遍历
user_list = [
    {"user_name": "unsc",
     "user_di": "001",
     "phone": "123123"},
    {"user_name": "root",
     "user_di": "002",
     "phone": "789789"
     }
]
for user_data in user_list:
    print(user_data)
