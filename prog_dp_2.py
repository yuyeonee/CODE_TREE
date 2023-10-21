def solution(triangle):
    answer = 0
    
    dp = triangle[:]
        
    for i in range(1, len(dp)):
        dp[i][0] += dp[i-1][0]
        dp[i][-1] += dp[i-1][-1]
    
    for i in range(2, len(dp)):
        for j in range(1, i):
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
            
    answer = max(dp[-1])        
    
    
    return answer
