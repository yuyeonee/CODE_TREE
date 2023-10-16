graph = [list(map(int, input().split())) for _ in range(19)]

direct = [(0, 1), (1, 0), (1, 1), (-1, 1)]

def in_range(x, y):
    return 0<=x<19 and 0<=y<19

def dfs(n, color, index, direction):
    global flag
    a, b = index[-2], index[-1]
    if n==4:
        print(color)
        print(index[4]+1, index[5]+1)
        flag = False
        return
    if n==0:
        for i in range(4):
            dx, dy = direct[i]
            nx, ny = a+dx, b+dy
            if in_range(nx, ny) and graph[nx][ny]==color:
                dfs(n+1, color, index+[nx,ny], i)
    else:
        dx, dy = direct[direction]
        nx, ny = a+dx, b+dy
        if in_range(nx, ny) and graph[nx][ny]==color:
            dfs(n+1, color, index+[nx,ny], direction)
        
flag = True
for i in range(19):
    for j in range(19):
        if graph[i][j]==1:
            dfs(0, 1, [i, j], -1)
        if graph[i][j]==2:
            dfs(0, 2, [i, j], -1)
if flag: print(0)


