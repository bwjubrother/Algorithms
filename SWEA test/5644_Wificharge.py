import sys

sys.stdin = open('5644.txt', 'r')

T = int(input())

for i in range(T):
    M, N = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    chargers = []
    for _ in range(N):
        chargers.append(list(map(int, input().split())))
    Ax, Ay = 1, 1
    Bx, By = 10, 10


    # 충전기 설치
    board = [[[] for _ in range(11)] for _ in range(11)]
    for idx, j in enumerate(chargers):
        for l in range(-j[2], 1):
            for o in range(-(j[2]+l), j[2]+l+1):
                if 1 <= j[1]+o <= 10 and 1 <= j[0]+l <= 10:
                    board[j[1]+o][j[0]+l].append(idx+1)
        for l in range(1, j[2]+1):
            for o in range(-(j[2]-l), j[2]-l+1):
                if 1 <= j[1]+o <= 10 and 1 <= j[0]+l <= 10:
                    board[j[1]+o][j[0]+l].append(idx+1)

    # 사람 진행
    sumA = []
    sumB = []
    for ago in A:
        if ago == 1:
            Ax -= 1
            sumA.append(board[Ax][Ay])
        elif ago == 2:
            Ay += 1
            sumA.append(board[Ax][Ay])
        elif ago == 3:
            Ax += 1
            sumA.append(board[Ax][Ay])
        elif ago == 4:
            Ay -= 1
            sumA.append(board[Ax][Ay])
        elif ago == 0:
            sumA.append(board[Ax][Ay])

    for go in B:
        if go == 1:
            Bx -= 1
            sumB.append(board[Bx][By])
        elif go == 2:
            By += 1
            sumB.append(board[Bx][By])
        elif go == 3:
            Bx += 1
            sumB.append(board[Bx][By])
        elif go == 4:
            By -= 1
            sumB.append(board[Bx][By])
        elif go == 0:
            sumB.append(board[Bx][By])

    ans = 0
    for q in range(len(A)):
        tmp = []
        if len(sumA[q]) == 0:
            for b in sumB[q]:
                tmp.append(chargers[b-1][3])
        elif len(sumB[q]) == 0:
            for a in sumA[q]:
                tmp.append(chargers[a-1][3])
        else:
            for a in sumA[q]:
                for b in sumB[q]:
                    if a == b:
                        tmp.append(chargers[a-1][3])
                    else:
                        tmp.append(chargers[a-1][3] + chargers[b-1][3])
        if len(tmp) != 0:
            ans += max(tmp)
    print('#%d %d' %(i+1, ans))