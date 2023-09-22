n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
ans_cnt = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(4):
            a = i + dx[k]
            b = j + dy[k]
            if 0<=a<n and 0<=b<n and graph[a][b]==1:
                count+=1
        if count>=3:
            ans_cnt+=1
print(ans_cnt)
