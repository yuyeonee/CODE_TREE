n = int(input())
graph = [[0]*n for _ in range(n)]

a, b = n//2, n//2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dir_num = 0
graph[a][b]=1

check = 2
flag = False
while 1:
    for i in range(check//2):
        if graph[a][b]==n*n:
            flag = True
            break
        x, y = a+dx[dir_num], b+dy[dir_num]
        graph[x][y] = graph[a][b]+1
        a, b = x, y
    check += 1
    if flag:
        break
        
    dir_num = (dir_num+1)%4

for i in range(n):
    print(*graph[i])
