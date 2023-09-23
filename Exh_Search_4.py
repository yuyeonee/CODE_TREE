n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))
max_sum = 0
for i in range(n):
    for j in range(n-2):
        cur_sum = graph[i][j]+graph[i][j+1]+graph[i][j+2]
        max_sum = max(max_sum, cur_sum)
print(max_sum)
