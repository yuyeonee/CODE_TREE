n, t = tuple(map(int, input().split()))
sequence = input()
graph = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dir_num = 0
a, b = n//2, n//2
score = graph[a][b]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

for task in sequence:
    if task=='F':
        x, y = a+dx[dir_num], b+dy[dir_num]
        if in_range(x, y):
            score += graph[x][y]
            a, b = x, y
    elif task=='L':
        dir_num = (dir_num+1)%4
    else:
        dir_num = (dir_num+3)%4

print(score)
