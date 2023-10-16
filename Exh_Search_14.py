N, M = map(int, input().split())
words = [list(input()) for _ in range(N)]

dX, dY = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0<=x<N and 0<=y<M

ans = 0
for i in range(N):
    for j in range(M):
        if words[i][j]=='L':
            for dx, dy in zip(dX, dY):
                cnt=0
                for k in range(1, 3):
                    nx, ny = i+dx*k, j+dy*k
                    if in_range(nx, ny) and words[nx][ny]=='E':
                        cnt += 1
                if cnt==2:
                    ans+=1

print(ans)
