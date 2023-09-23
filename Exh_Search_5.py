r, c = map(int, input().split())
graph = list(list(input().split()) for _ in range(r))

a, b = 0, 0
cnt = 0
for i in range(1, r-2):
    for j in range(1, c-2):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if graph[a][b]!=graph[i][j] and graph[i][j]!=graph[k][l] and graph[k][l]!=graph[r-1][c-1]:
                    cnt+=1
print(cnt)
