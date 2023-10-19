from collections import defaultdict

def solution(participant, completion):
    answer = ''
    dict = defaultdict(int)
    for p in participant:
        dict[p] += 1

    for c in completion:
        dict[c] -= 1

    for k, v in dict.items():
        if v == 1:
            answer = k

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))