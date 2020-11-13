i = 0
while i < 100:
    if i == 3:
        i += 1
        print("i=3不进行输出")
        continue
    if i == 10:
        print('到10了跳出循环')
        break
    print(i)

    i += 1
print("结束")
