n, m = tuple(map(int, input().split()))
graph = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
graph[0][0] = chr(65)
a, b, cnt = 0, 0, 0
while 1:
    if cnt==n*m-1:
        break
    x, y = a + dx[dir_num], b + dy[dir_num]
    if 0<=x<n and 0<=y<m and graph[x][y]==0:
        cnt+=1
        graph[x][y] = chr((cnt%26) + 65)
        a, b = x, y
    else:
        dir_num = (dir_num+1)%4

for i in range(n):
    print(*graph[i])
