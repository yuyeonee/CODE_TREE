sequence = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
a, b, cnt = 0, 0, 0
flag = False
for task in sequence:
    if task == 'F':
        #go
        x = a + dx[(dir_num+4)%4]
        y = b + dy[(dir_num+4)%4]
        a, b = x, y
    else:
        if task=='R':
            dir_num+=1
        else:
            dir_num-=1
    cnt+=1

    if x==0 and y==0:
        flag = True
        break
print(cnt if flag else -1)


        
