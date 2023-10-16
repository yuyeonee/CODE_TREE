n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+2, n):
        s = nums[i]+nums[j]
        ans = max(ans, s)

print(ans)
