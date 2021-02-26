import sys
sys.stdin = open('17135.txt', 'r')

from itertools import combinations

n, m, d = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
kill = 0
# 궁수 3명 최적 배치
    for item in combinations(range(m), 3):
        for ix in item:
            # 제거하기
            for y in range(n-1, -1, -1):
                flag = 0
                for x in range(m):
                    if board[x][y] == 1 and (y + abs(x-ix)) <= d:
                        board[x][y] = 0
                        flag = 1
                        break
                if flag == 1:
                    break

# 아래로 한 칸 내리기
board = board[:-1]