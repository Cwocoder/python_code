# 给定一个数 a，判断一个数字是否为奇数或偶数。
while True:
    try:
        num = int(input('输入一个整数：'))
    except ValueError:
        print("输入的不是整数！")
        continue
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')
    break
