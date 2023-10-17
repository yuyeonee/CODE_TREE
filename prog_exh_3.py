import math

def solution(brown, yellow):
    answer = []
    all_piece = brown+yellow
    
    for i in range(3, int(math.sqrt(all_piece))+1):
        if all_piece%i==0:
            a, b = all_piece//i, i
            if (a-1)*2+(b-1)*2==brown:
                return [a, b]
    
    return [a, b]
