# "百马百担"问题：一匹大马能驮3担货，一匹中马能驮2担货，两匹小马能驮1担货，如果用一百匹马驮一百担货，问有大、中、小马各几匹？
# 假设大马有x,假设中马有y,小马  100 - x - y
for x in range(0,100//3+1):
    for y in range(0,100//2+1):
        if 3*x+2*y+(100-x-y)*0.5 == 100:
            print(x,y,(100-x-y))
