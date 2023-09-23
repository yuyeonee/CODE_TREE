n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
color = list(map(int, input().split()) for _ in range(m))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for a, b in color:
    a, b = a-1, b-1
    graph[a][b] = 1
    cnt = 0
    for i in range(4):
        x, y = a+dx[i], b+dy[i]
        if 0<=x<n and 0<=y<n and graph[x][y]==1:
            cnt+=1
    print(1 if cnt==3 else 0)
