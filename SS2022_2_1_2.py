#7:20
from collections import deque

q = int(input())
establish = list(map(int, input().split()))

n, m = establish[1], establish[2]
belt = [None]*m
for i in range(m):
    belt[i] = deque()

items = establish[3:]
temp = n//m
for i in range(len(items)//2):
    belt[i//temp].append([items[i], items[i+n]])

def down(w_max):
    global belt
    w_sum = 0
    for i in range(m):
        if belt[i]:
            r_id, w = belt[i].popleft()
        else:
            continue
        if w<=w_max:
            w_sum += w
        else:
            belt[i].append([r_id, w])
    return w_sum

def eliminate(r_id):
    global belt

    for i in range(m):
        for j in range(len(belt[i])):
            if r_id in belt[i][j]:
                belt[i].remove(belt[i][j])
                return r_id
    return -1

def find(f_id):
    global belt
    for i in range(m):
        for j in range(len(belt[i])):
            if belt[i][j][0]==f_id:
                for _ in range(j, len(belt[i])):
                    belt[i].appendleft(belt[i].pop())
                return i+1

    return -1

broken_num = []
def broken(b_num):
    global belt
    global broken_num
    if (b_num-1) in broken_num:
        return -1
    else:
        broken_num.append(b_num-1)
        check_num = (b_num%m)
        while 1:
            if check_num in broken_num:
                continue
            else:
                for i in range(len(belt[b_num-1])):
                    belt[check_num].append(belt[b_num-1].popleft())
                return b_num
            check_num = (check_num+1)%m
    return -1
        


for _ in range(q-1):
    comm, n = map(int, input().split())
    if comm==200:
        print(down(n))
    elif comm==300:
        print(eliminate(n))
    elif comm==400:
        print(find(n))
    elif comm==500:
        print(broken(n))
