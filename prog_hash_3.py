from collections import defaultdict
from collections import Counter

def solution(clothes):
    answer = 0
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1

    ans = 1
    for v in dic.values():
        ans *= (v+1)
    answer = ans-1
    
    return answer
