n = int(input())
nums = [int(input()) for _ in range(n)]
ans = -1
s = 0

def check(a, b, c):

    while (a+b+c)!=0:
        a_r, b_r, c_r = a%10, b%10, c%10
        if (a_r+b_r+c_r)>=10:
            return False
        a, b, c = a//10, b//10, c//10
    return True



for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if check(nums[i], nums[j], nums[k]):
                s = nums[i]+nums[j]+nums[k]
                ans = max(ans, s)

print(ans)
