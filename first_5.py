n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
a, b = 0, 0
graph[0][0] = 1
dir_num = 0
while 1:
    if graph[a][b]==n*m:
        break
    x = a + dx[dir_num]
    y = b + dy[dir_num]
    if 0<=x<n and 0<=y<m and graph[x][y]==0:
        graph[x][y] = graph[a][b] + 1
        a, b = x, y
    else:
        dir_num+=1
        dir_num = dir_num%4

for i in range(n):
    print(*graph[i])
