from collections import deque

def solution(begin, target, words):
    answer=0
    
    queue = deque()
    n = len(begin)
    queue.append((begin, [], 0))
    
    while queue:
        st, visited, ans = queue.popleft()
        for idx, word in enumerate(words):
            cnt=0
            for i, s in enumerate(word):
                if s==st[i]:
                    cnt+=1
            if cnt==n-1 and (word not in visited):
                queue.append((word, visited+[word], ans+1))
        
        if st==target:
            print(ans)
            answer = ans
            break
        
        if len(visited)==len(words):
            break
            
    return answer
