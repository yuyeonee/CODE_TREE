n = int(input())
graph = list(input() for _ in range(n))
k = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = (k-1)//n
if dir_num==0:
    a, b = 0, (k-1)
elif dir_num==1:
    a, b = (k-1)%n, n-1
elif dir_num==2:
    a, b = n-1, (n-1)-(k-1)%n
else:
    a, b= (n-1)-(k-1)%n, 0

cnt=0
while 1:
    cnt+=1
    if graph[a][b]=='/':
        if dir_num<2:
            dir_num = 1-dir_num
        else:
            dir_num = 5-dir_num
    if graph[a][b]=='\\':
        dir_num = 3-dir_num
    x, y = a + dx[dir_num], b + dy[dir_num]
    if 0<=x<n and 0<=y<n:
        a, b = x, y
    else:
        break
print(cnt)
