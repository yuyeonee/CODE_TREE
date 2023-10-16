import sys

N = int(input())
nums = list(int(input()) for _ in range(N))
all_p = sum(nums)

ans = sys.maxsize
for j in range(N):
    dist = 0
    for i in range(N):
        dist += nums[(i+j)%N]*i
    ans = min(ans, dist)
print(ans)
