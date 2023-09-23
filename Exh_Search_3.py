n = int(input())
cows = list(map(int, input().split()))
cnt = 0
num = len(cows)
for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            if cows[i]<=cows[j]<=cows[k]:
                cnt+=1

print(cnt)
