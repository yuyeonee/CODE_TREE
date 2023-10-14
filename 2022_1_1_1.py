
n, m, h, k = map(int, input().split())
domangs = [list(map(int, input().split())) for _ in range(m)]
trees = [list(map(int, input().split())) for _ in range(h)]

for domang in domangs:
    domang[2] -= 1 # 1은 direction=0 2는 direction=1

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(x, y):
    return 1<=x<=n and 1<=y<=n

def running(finder):
    new_domangs=[]
    f_x, f_y = finder # 술래 위치
    for domang in domangs: # 도망자 한 명씩
        a, b = domang[0], domang[1]
        if (abs(f_x-a)+abs(f_y-b))<=3: # 술래와 거리 3 이하면
            nx, ny = a+direct[domang[2]][0], b+direct[domang[2]][1] # 1칸 이동
            if not in_range(nx,ny): # 격자 외
                domang[2] = (domang[2]+2)%4 # 방향 전환
                nx, ny = a + direct[domang[2]][0], b + direct[domang[2]][1] # 1칸 이동
                if [nx,ny]!=[f_x,f_y]:
                    new_domangs.append([nx,ny, domang[2]])
                else:
                    new_domangs.append([a,b, domang[2]])
            elif in_range(nx,ny) and [nx,ny]!=[f_x,f_y]: # 격자 내면서 술래 위치가 아니면
                new_domangs.append([nx,ny, domang[2]]) # new에 추가
            else:
                new_domangs.append([a, b, domang[2]])
        else:
            new_domangs.append([a, b, domang[2]])
    return new_domangs

def move_finder_f(finder): # 정방향
    global finder_d_num, flag
    a, b = finder # 기존 술래 위치
    nx, ny = a+direct[finder_d_num][0], b+direct[finder_d_num][1] # 술래 방향 한 칸 앞으로
    if in_range(nx, ny): # 정상적 위치면
        visited[nx][ny]=False # 방문 처리
        a, b = nx, ny # 위치 변경
        if visited[a+direct[(finder_d_num+1)%4][0]][b+direct[(finder_d_num+1)%4][1]]: # 변경 위치의 오른쪽이 비었다면
            finder_d_num = (finder_d_num+1)%4 # 방향 오른쪽으로 회전 (시야 변경)
    if nx==1 and ny==1: # 1,1로 가면
        finder_d_num = 1 # 아래방향으로 변경
        flag = False # 다음 move부터 move_finder_b으로 변경
        # visited 초기화
        for i in range(n+1):
            for j in range(n+1):
                visited[i][j] = True
        visited[nx][ny] = False
    return [nx,ny]

def move_finder_b(finder): # 역방향
    #global finder_d_num, flag
    a, b = finder # 기존 술래 위치
    nx, ny = a+direct[finder_d_num][0], b+direct[finder_d_num][1] # 앞으로 1칸
    if in_range(nx,ny):
        visited[nx][ny] = False
        a, b = nx, ny
        cx, cy = a + direct[finder_d_num][0], b + direct[finder_d_num][1]  # 앞으로 1칸
        if not in_range(cx, cy) or visited[cx][cy]==False: # 격자 밖이거나 갔던 곳이면
            finder_d_num = (finder_d_num+3)%4 # 방향 왼쪽으로 회전
    if nx==n//2+1 and ny==n//2+1: # 중심으로 돌아오면
        finder_d_num=3 # 위로 방향 변경
        flag = True # 다음 move부터 move_finder_f로 실행
        for i in range(n+1): # visited 초기화
            for j in range(n+1):
                visited[i][j] = True
        visited[nx][ny]=False

    return [nx,ny]

def find(finder, round): # 술래잡기
    a, b = finder # 술래 위치
    get_score = 0
    remove_index = []
    if [a,b] not in trees: # 술래 위치 점검 (나무가 아니라면)
        for i in range(len(domangs)): # 도망자 중에
            if a == domangs[i][0] and b == domangs[i][1]: # 술래 위치에 있다면
                remove_index.append(domangs[i])  # 도망자 제거
                get_score += (round + 1) # 점수 추가
    for i in range(2): # 술래 위치 제외 나머지 2칸 시야 점검
        nx, ny = a+direct[finder_d_num][0]*(i+1), b+direct[finder_d_num][1]*(i+1)
        if in_range(nx,ny): # 격자 안이면
            if [nx,ny] in trees: # 나무 있으면 점검 불가
                continue # 패스
            for j in range(len(domangs)): # 나무 없으면 도망자 중에
                if nx==domangs[j][0] and ny==domangs[j][1]: # 시야에 있으면
                    remove_index.append(domangs[j])
                    get_score+=(round+1)
        else:
            break
    print(remove_index)
    arr_new = [i for i in domangs if i not in remove_index]

    return get_score, arr_new



finder_d_num = 3
fa, fb = n//2+1, n//2+1
visited = [[True] * (n + 1) for _ in range(n + 1)]
visited[fa][fb] = False
flag = True
finder = [fa, fb]
total_score=0
for i in range(k):
    print(i+1)
    domangs = running(finder) # 도망자 이동
    if flag:
        finder = move_finder_f(finder) # 정방향 술래이동
    else:
        finder = move_finder_b(finder) # 역방향 술래이동
    # print(finder, 'finder')
    # print(domangs, 'domangs')
    # print(finder_d_num)

    score, new_domang = find(finder, i) # 술래잡기
    domangs = new_domang # 도망자 수정
    total_score += score # 점수 추가

print(total_score)

