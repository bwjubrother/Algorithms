import sys

sys.stdin = open('5644.txt', 'r')

T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    p_A = [0] + list(map(int, input().split()))
    p_B = [0] + list(map(int, input().split()))
    charge = [list(map(int, input().split())) for _ in range(A)] # 충전기 정보
    # c[i] = [c = x, r = y, 충전 범위, 성능]
    p = [[0]*11 for _ in range(11)]
    area = []
    for x, y, C, P in charge:
        temp = []
        for j in range(-C, C+1):
            if 1 <= y+j <= 10:
                for c in range(x-(C-abs(j)), x+(C-abs(j))+1):
                    if 1 <= c <= 10:
                        p[y+j][c] += 1
                        temp.append([c, y+j])
        area.append(temp)

    dr = [0, -1, 0, 1, 0] # x 상 우 하 좌
    dc = [0, 0, 1, 0, -1]
    total = 0
    r_A, c_A = 1, 1
    r_B, c_B = 10, 10
    for m in range(M+1):
        tr_A = r_A + dr[p_A[m]]
        tc_A = c_A + dc[p_A[m]]
        tr_B = r_B + dr[p_B[m]]
        tc_B = c_B + dc[p_B[m]]
        r_A, c_A, r_B, c_B = tr_A, tc_A, tr_B, tc_B
        current_A, current_B = [], [] # 몇 번째 영역 안에 있는지
        for i in range(A):
            if [tc_A, tr_A] in area[i]:
                current_A.append(i)
            if [tc_B, tr_B] in area[i]:
                current_B.append(i)
        scores = []
        if not current_B:
            for x in current_A:
                scores.append(charge[x][-1])
        elif not current_A:
            for x in current_B:
                scores.append(charge[x][-1])
        for i in range(len(current_A)):
            for j in range(len(current_B)):
                if current_A[i] == current_B[j]:
                    scores.append((charge[current_A[i]][-1] + charge[current_B[j]][-1]) / 2)
                else:
                    scores.append(charge[current_A[i]][-1] + charge[current_B[j]][-1])
        if scores:
            total += max(scores)
            print(total)
    print('#{0} {1}'.format(t, int(total)))
