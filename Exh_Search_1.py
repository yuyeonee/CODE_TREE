import sys

n = int(input())
house = list(map(int, input().split()))
min_sum = sys.maxsize

for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += (abs(i-j)*house[j])
    if min_sum>sum_diff:
        min_sum = sum_diff

print(min_sum)
