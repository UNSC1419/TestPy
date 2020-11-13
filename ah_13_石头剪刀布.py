import random
玩家数 =int(input("请输入您要出的拳 1/石头 2/剪刀 3/布："))
电脑数 = random.randint(1, 3)
if ((玩家数 == 1 and 电脑数 == 2)
        or (玩家数 == 2 and 电脑数 == 3)
        or (玩家数 == 3 and 电脑数 == 1)):
    print("您赢了")
elif 玩家数 == 电脑数:
    print("平局了")
else:
   print("您输了")
