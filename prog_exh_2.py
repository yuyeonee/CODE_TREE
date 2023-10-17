def solution(answers):
    answer = []
    p = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct = [0]*3
    for i in range(len(answers)):
        for j in range(3):
            if answers[i]==p[j][i%len(p[j])]:
                correct[j]+=1
   
    f = max(correct)
    for i in range(3):
        if correct[i]==f:
            answer.append(i+1)
    
    return answer
