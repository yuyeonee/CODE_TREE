n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

a, b = 0, 0
for i in range(n):
    way, num = input().split()
    if way=="E":
        index = 0
    elif way=="W":
        index = 1
    elif way == "S":
        index = 2
    else:
        index = 3
    
    a, b = a+dx[index]*int(num), b+dy[index]*int(num)
print(a, b)
