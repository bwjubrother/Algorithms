import sys
from collections import deque
sys.stdin = open('4130.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    ips = [list(map(int, input().split())) for _ in range(n)]
    for ip in ips:
        #첫번째 자석
        if ip[0] == 1:
            #우회전시
            if ip[1] == 1:
                magnets[0].rotate(1)
                if magnets[1][-2] != magnets[0][3]:
                    magnets[1].rotate(-1)
                    if magnets[2][-2] != magnets[1][1]:
                        magnets[2].rotate(1)
                        if magnets[3][-2] != magnets[2][3]:
                            magnets[3].rotate(-1)
            #좌회전시
            elif ip[1] == -1:
                magnets[0].rotate(-1)
                if magnets[1][-2] != magnets[0][1]:
                    magnets[1].rotate(1)
                    if magnets[2][-2] != magnets[1][3]:
                        magnets[2].rotate(-1)
                        if magnets[3][-2] != magnets[2][1]:
                            magnets[3].rotate(1)
        #두번째 자석
        if ip[0] == 2:
            #우회전시
            if ip[1] == 1:
                magnets[1].rotate(1)
                if magnets[0][2] != magnets[1][-1]:
                    magnets[0].rotate(-1)
                if magnets[2][-2] != magnets[1][3]:
                    magnets[2].rotate(-1)
                    if magnets[3][-2] != magnets[2][1]:
                        magnets[3].rotate(1)
            #좌회전시
            elif ip[1] == -1:
                magnets[1].rotate(-1)
                if magnets[0][2] != magnets[1][-3]:
                    magnets[0].rotate(1)
                if magnets[2][-2] != magnets[1][1]:
                    magnets[2].rotate(1)
                    if magnets[3][-2] != magnets[2][3]:
                        magnets[3].rotate(-1)
        #세번째 자석
        if ip[0] == 3:
            #우회전시
            if ip[1] == 1:
                magnets[2].rotate(1)
                if magnets[3][-2] != magnets[2][3]:
                    magnets[3].rotate(-1)
                if magnets[1][2] != magnets[2][-1]:
                    magnets[1].rotate(-1)
                    if magnets[0][2] != magnets[1][-3]:
                        magnets[0].rotate(1)
            #좌회전시
            elif ip[1] == -1:
                magnets[2].rotate(-1)
                if magnets[3][-2] != magnets[2][1]:
                    magnets[3].rotate(1)
                if magnets[1][2] != magnets[2][-3]:
                    magnets[1].rotate(1)
                    if magnets[0][2] != magnets[1][-1]:
                        magnets[0].rotate(-1)
        # 네번째 자석
        if ip[0] == 4:
            # 우회전시
            if ip[1] == 1:
                magnets[3].rotate(1)
                if magnets[2][2] != magnets[3][-1]:
                    magnets[2].rotate(-1)
                    if magnets[1][2] != magnets[2][-3]:
                        magnets[1].rotate(1)
                        if magnets[0][2] != magnets[1][-1]:
                            magnets[0].rotate(-1)
            # 좌회전시
            elif ip[1] == -1:
                magnets[3].rotate(-1)
                if magnets[2][2] != magnets[3][-3]:
                    magnets[2].rotate(1)
                    if magnets[1][2] != magnets[2][-1]:
                        magnets[1].rotate(-1)
                        if magnets[0][2] != magnets[1][-3]:
                            magnets[0].rotate(1)
    ans = magnets[0][0] + 2 * magnets[1][0] + 4 * magnets[2][0] + 8 * magnets[3][0]
    print('#%d %d' % (tc+1, ans))

'''
# Better solution
T = int(input())
for test_case in range(1, 1 + T):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        idx, rot = map(int, input().split())
        idx -= 1  # 0 ~ 3번 톱니
        move = [(idx, rot)]  # 돌릴 톱니

        # 왼쪽 톱니 확인
        temp = rot
        for i in range(idx - 1, -1, -1):
            if mag[i][2] != mag[i + 1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 오른쪽 톱니 확인
        temp = rot
        for i in range(idx + 1, 4):
            if mag[i][6] != mag[i - 1][2]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        # 톱니 돌림
        for idx, rot in move:
            if rot == 1:
                mag[idx] = [mag[idx].pop()] + mag[idx]
            elif rot == -1:
                mag[idx].append(mag[idx].pop(0))

    # 결과 계산
    result = 0
    for i in range(4):
        result += mag[i][0] * 2**i

    print('#{} {}'.format(test_case, result))
'''