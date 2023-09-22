# 문자에 따른 명령 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
a, b = 0, 0
lrf = input()
dir = 0
for alpha in lrf:
    if alpha=='L':
        dir += 1
    elif alpha=='R':
        dir -= 1
    else:
        dir = dir%4
        a = a + dx[dir]
        b = b + dy[dir]

print(a, b)
