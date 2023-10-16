string = input()

cnt=0
for i in range(len(string)-3):
    if string[i]==string[i+1]=='(':
        for j in range(i+2, len(string)-1):
            if string[j]==string[j+1]==')':
                cnt+=1

print(cnt)
