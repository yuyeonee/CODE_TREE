from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    
    dic = defaultdict(int)
    
    for i, n in enumerate(name):
        dic[n] = yearning[i]
    
    for ph in photo:
        ans = 0
        for name in ph:
            ans += dic[name]
        answer.append(ans)
    
    return answer
