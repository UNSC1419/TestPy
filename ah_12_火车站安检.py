车票 = True
刀长度 = 19

if 车票:
    print("车票检查通过，准备开始安检")
    if 刀长度 < 20:
        print("安检通过，祝您旅途愉快")
    else:
        print("您的刀太长了，有%d公分长"%刀长度)
else:
    print("请先购买车票")