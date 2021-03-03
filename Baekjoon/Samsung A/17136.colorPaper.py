import sys
sys.stdin = open('17136.txt', 'r')

'''
from copy import deepcopy 

board = [list(map(int, input().split())) for _ in range(10)]

# 정사각형이 되는지 판별
def square(size, i, j):
    global board
    _board = deepcopy(board)
    for x in range(i, i+size):
        for y in range(j, j+size):
            if not _board[x][y]:
                return False
            else:
                _board[x][y] = 0
    # 찾았으면 0으로 붙임처리 갱신
    board = _board
    return True

def search():
    cntSum = 0
    # 크기 5x5 부터 정사각형 찾기
    for size in range(5, 0, -1):
        cnt = 0
        for i in range(10-size+1):
            for j in range(10-size+1):
                if board[i][j]:
                    if square(size, i, j):
                        cnt += 1
                    # 한 종류가 5개 이상이면 -1
                    if cnt > 5:
                        return -1
        cntSum += cnt
    # 남아있는 것이 있으면 -1
    for i in range(10):
        for j in range(10):
            if board[i][j]:
                return -1
    return cntSum

print(search())
'''

def solve(x, y, cnt):
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return
    
    if x >= 10:
        solve(0, y+1, cnt)
        return

    if board[x][y]:
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    if not board[i][j]:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        board[i][j] = 0

                paper[k] += 1
                solve(x+k+1, y, cnt+1)
                paper[k] -= 1

                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        board[i][j] = 1
    else:
        solve(x+1, y, cnt)


board = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = 26
solve(0, 0, 0)
print(ans) if ans != 26 else print(-1)