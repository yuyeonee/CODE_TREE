def solution(n):
    answer = []
        
    def dfs(dep, ans):
        if dep==(2*n)-1:
            answer.append(ans)
            return
        
        if ans.count('(')<n:
            dfs(dep+1, ans+'(')
        if ans.count('(') and ans.count('(')>ans.count(')'):
            dfs(dep+1, ans+')')
        
    dfs(0, '(')
    
    
    return len(answer)
