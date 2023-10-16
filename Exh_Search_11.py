n = int(input())
string = input()
cnt=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if string[i]=='C' and string[j]=='O' and string[k]=='W':
                cnt+=1
print(cnt)
