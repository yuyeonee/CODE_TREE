n = int(input())
cp = list(list(map(int, input().split())) for _ in range(n))
ans = []

for i in range(1, n-1):
    cp_sum = 0
    for j in range(n-1):
        if j==i-1:
            continue
        elif j==i:
            cp_sum += (abs(cp[j-1][0]-cp[j+1][0]) + abs(cp[j-1][1]-cp[j+1][1]))
        else:
            cp_sum += (abs(cp[j][0]-cp[j+1][0]) + abs(cp[j][1]-cp[j+1][1]))
    ans.append(cp_sum)
print(min(ans))
