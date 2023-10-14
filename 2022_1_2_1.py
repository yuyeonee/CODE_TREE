n, m, k = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def detect_head(): # 머리 찾기
    # print('detect_head')
    heads = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                heads.append((i, j))
    return heads

def detect_teammates(head): # 모든 팀원 찾기
    # print('detect_teammates')
    a, b = head
    teammates = [(a,b)]
    while graph[a][b]!=3:
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = a+dx, b+dy
            if in_range(nx, ny) and (graph[nx][ny]==2) and (nx,ny) not in teammates:
                teammates.append((nx, ny))
                a, b = nx, ny
                break
            if in_range(nx, ny) and teammates!=[(a,b)] and (graph[nx][ny] == 3) and (nx, ny) not in teammates:
                teammates.append((nx, ny))
                a, b = nx, ny
                break
    print(teammates)
    return teammates

def move_team(teammates):
    # print('move_team')
    a, b = teammates[0]
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = a + dx, b + dy
        if in_range(nx, ny) and graph[nx][ny] in [3, 4]:
            print(graph[nx][ny])
            print(teammates)
            if graph[nx][ny] == 3:
                teammates = teammates[:-1]
            for teammate in teammates:
                cx, cy = teammate
                graph[nx][ny], graph[cx][cy] = graph[cx][cy], graph[nx][ny] # 값 바꾸기
                nx, ny = cx, cy
                # print('cc')
            break

def throw_ball(round): # n=7일 때 round 0-27
    # print('throw_ball')
    print(round, 'round')
    way = round//n # 탐색 방향
    num = round%n  # 시작 위치
    s_x, s_y = -1, -1

    if way==0: # 가로줄 탐색 왼 -> 오
        for i in range(n):
            if graph[num][i] in [1, 2, 3]:
                s_x, s_y = num , i
                break
    if way==1: # 세로줄 탐색 아래 -> 위
        for i in range(n-1, -1, -1):
            if graph[i][num] in [1, 2, 3]:
                s_x, s_y = i, num
                break
    if way==2: # 가로줄 탐색 오 -> 왼
        for i in range(n-1, -1, -1):
            if graph[n-num-1][i] in [1, 2, 3]:
                s_x, s_y = n-num-1, i
                break
    if way==3: # 세로줄 탐색 위 -> 아래
        for i in range(n):
            if graph[i][n-num-1] in [1, 2, 3]:
                s_x, s_y = i, n-num-1
                break
    print(s_x, s_y)
    if (s_x, s_y)==(-1, -1): # 공에 맞은 사람이 없을 때
        return 0, (s_x, s_y) # 0점 return

    for i in range(len(heads)): # head 중에서
        teammates = detect_teammates(heads[i])
        if (s_x, s_y) in teammates: # 공맞은 사람이 있는 팀
            get_score_head = i
            get_score = (teammates.index((s_x, s_y)))+1 # 맞은 사람 순서 1부터
            print(get_score)
            break


    return get_score**2 , get_score_head # 점수, 맞은 사람 팀 index 리턴

def switch_head(head):
    #print('switch_head')
    teammates = detect_teammates(heads[head])
    hx, hy = teammates[0]
    tx, ty = teammates[-1]
    graph[hx][hy], graph[tx][ty] = graph[tx][ty], graph[hx][hy]


total_score = 0
for round in range(k):
    heads = detect_head() # head 찾기
    for head in heads: # head 마다
        move_team(detect_teammates(head)) # 모든 팀원 찾고 팀원 이동시키기
        for i in range(n):
            print(*graph[i])
    heads = detect_head() # 바뀐 head 위치 저장

    score, get_score_head = throw_ball(round%(n*4)) # round에 맞기 공 던지기 실시
    if score!=0:
        total_score += score
        switch_head(get_score_head)
    for i in range(n):
        print(*graph[i])
    print(total_score)

print(total_score)
