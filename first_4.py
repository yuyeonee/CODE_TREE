n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

direction = {
    'R': 0,
    'L': 3,
    'U': 2,
    'D': 1
}
dir_num = direction[d]

for i in range(t):
    a, b = r + dy[dir_num], c + dx[dir_num]
    if 1<=a<=n and 1<=b<=n:
        r, c = a, b
    else:
        dir_num = 3 - dir_num
print(r, c)

