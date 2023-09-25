from collections import defaultdict

belt_info = defaultdict(lambda: -1)
prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)
weight = {}

head, tail = [0 for _ in range(10)], [0 for _ in range(10)]
parent_belt = [i for i in range(10)]
broken = [False for _ in range(10)]

n, m = -1, -1

def build_fac(_n, _m, etc):
    global belt_info, prv, nxt, weight, head, tail, parent_belt, broken, n, m

    belt_info = defaultdict(lambda: -1)
    prv, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)
    weight = {}

    head, tail = [0 for _ in range(10)], [0 for _ in range(10)]
    parent_belt = [i for i in range(10)]
    broken = [False for _ in range(10)]

    n, m = _n, _m
    temp_id, temp_w = etc[:n], etc[n:]

    for i in range(n):
        weight[temp_id[i]] = temp_w[i]

    size = n//m
    for i in range(m):
        head[i] = temp_id[i*size]
        tail[i] = temp_id[(i+1)*size - 1]

        for j in range(i*size, (i+1)*size):
            belt_info[temp_id[j]] = i

            #???
            if j<(i+1)*size-1:
                nxt[temp_id[j]] = temp_id[j+1]
                prv[temp_id[j+1]] = temp_id[j]


def remove_id(_id, remove_belt):
    b = belt_info[_id]
    b_num = parent_belt[b]

    if remove_belt:
        belt_info[_id] = -1

    if head[b_num] == tail[b_num]:
        head[b_num] = tail[b_num] = 0
    elif head[b_num] == _id:
        n_id = nxt[_id]
        head[b_num] = n_id
        prv[n_id] = 0
    elif tail[b_num] == _id:
        p_id = prv[_id]
        tail[b_num] = p_id
        nxt[p_id] = 0
    else:
        n_id = nxt[_id]
        p_id = prv[_id]
        nxt[p_id] = n_id
        prv[n_id]  = p_id

    prv[_id] = nxt[_id] = 0

def down(w_max):
    total = 0
    for i in range(m):
        if broken[i] or head[i]==0:
            continue
        d_id = head[i]
        w = weight[d_id]

        if w<=w_max:
            total+=w

            remove_id(d_id, True)
        elif nxt[d_id] != 0:
            remove_id(d_id, False)
            
            tail_id = tail[i]
            prv[d_id] = tail_id
            nxt[tail_id] = d_id
            tail[i] = d_id
    print(total)

def eliminate(e_id):
    if belt_info[e_id] == -1:
        print(-1)
        return
    remove_id(e_id, True)
    print(e_id)

def find(f_id):
    if belt_info[f_id] == -1:
        print(-1)
        return
    
    b = belt_info[f_id]
    b_num = parent_belt[b]

    if head[b_num] != f_id:
        ori_tail = tail[b_num]
        ori_head = head[b_num]

        now_tail = prv[f_id]
        tail[b_num] = now_tail
        nxt[now_tail] = 0

        nxt[ori_tail] = ori_head
        prv[ori_head] = ori_tail

        head[b_num] = f_id
    print(b_num+1)

def broke(b_num):
    b_num -= 1
    if broken[b_num]:
        print(-1)
        return
    
    broken[b_num] = True

    if head[b_num] == 0:
        print(b_num+1)
        return
    
    nxt_num = b_num
    while True:
        nxt_num = (nxt_num+1)%m
        if not broken[nxt_num]:
            if tail[nxt_num] == 0:
                head[nxt_num] = head[b_num]
                tail[nxt_num] = tail[b_num]

            else:
                b_head = head[b_num]
                nxt_tail = tail[nxt_num]
                nxt[nxt_tail] = b_head
                prv[b_head] = nxt_tail

                tail[nxt_num] = tail[b_num]
            break
    
    for i in range(m):
        if parent_belt[i]==b_num:
            parent_belt[i] = nxt_num
    
    print(b_num+1)



q = int(input())
for _ in range(q):
    comm = list(map(int, input().split()))
    if comm[0]==100:
        build_fac(comm[1], comm[2], comm[3:])
    elif comm[0]==200:
        down(comm[1])
    elif comm[0]==300:
        eliminate(comm[1])
    elif comm[0]==400:
        find(comm[1])
    else:
        broke(comm[1])
    
    print()
    print(comm)
    print("prv : ", prv)
    print("nxt : ", nxt)
    print("weight : ", weight)
    print("belt_info : ", belt_info)

    print("head : ", head)
    print("tail : ", tail)

    print("parent_belt : ", parent_belt)
    print("broken : ", broken)
    print()



