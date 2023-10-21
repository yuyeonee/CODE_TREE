from collections import deque

def solution(N, number):
    if N==number:
        return 1
    answer = 0
    flag = True
    
    dp = [set() for _ in range(8)]
    
    for idx, d in enumerate(dp):
        d.add(int(str(N)*(idx+1)))
        
    for i in range(1, 8):
        for j in range(i):
            for s1 in dp[j]:
                for s2 in dp[i-j-1]:
                    dp[i].add(s1 + s2)
                    dp[i].add(s1 * s2)
                    dp[i].add(s1 - s2)
                    if s2!=0:
                        dp[i].add(s1//s2)
                    
        if number in dp[i]:
            answer = i+1
            flag = False
            break
    
    if flag:
        answer = -1
    
    return answer
