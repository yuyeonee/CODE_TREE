n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

direction = {
    'N': 2,
    'S': 3,
    'E': 0,
    'W': 1
}

a, b = 0, 0
cnt = 0
flag = False
for i in range(n):
    dire, num = input().split()
    dir_num = direction[dire]
    num = int(num)

    for j in range(num):
        x, y = a + dx[dir_num], b + dy[dir_num]
        cnt += 1
        a, b = x, y

        if x==0 and y==0:
            flag = True
            break
    if flag:
        break
        
print(cnt if flag else -1)
