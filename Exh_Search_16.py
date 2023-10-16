import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = sys.maxsize
s_nums = sum(nums)

for i in range(N):
    for j in range(i+1, N):
        s = s_nums - nums[i] - nums[j]
        ans = min(ans, abs(S-s))
print(ans)

