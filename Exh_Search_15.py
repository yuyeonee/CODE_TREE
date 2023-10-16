N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N): # 한 줄에 있지 않을 때
    for j in range(N-2):
        s = sum(graph[i][j:j+3])
        for k in range(i+1, N):
            for l in range(N-2):
                s2 = sum(graph[k][l:l+3])
                ans = max(ans, s+s2)

for i in range(N): # 한 줄에 있을 때
    for j in range(N-5):
        ss = sum(graph[i][j:j+3])
        for k in range(j+3, N-2):
            ss2 = sum(graph[i][k:k+3])
            ans = max(ans, ss+ss2)

print(ans)
