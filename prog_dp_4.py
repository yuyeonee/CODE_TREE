import sys

def solution(arr):
    n = len(arr)//2
    dp = [0]*(n)
    #dp[0] = -sys.maxsize
    temp = [[] for _ in range(n*2)]
    print(temp)
    
    ans = 0
    for i in range(0, 2*n, 2):
        a = int(arr[-(i+1)])
        op = arr[-(i+2)]
        print(a, op)
        if op=='-':
            temp[i//2].append(ans-a)
        if op=='+':
            temp[i//2].append(ans + a)
        print(temp)
        print(dp)
        for num in temp[i//2-1]:
            if op=='-':
                temp[i].append(ans-a)
                temp[i].append(-(a+num))
                # dp[i//2] = max(-(dp[(i-2)//2]+a), ans-a)
            if op=='+':
                temp[i].append(ans+a)
                #dp[i//2] = (ans+a)
        #     print(temp)
        #     print(dp)
        ans = dp[i//2]    

    return int(arr[0]) + ans
