import sys
sys.stdin = open('1018.txt', 'r')

N, M = map(int, input().split(' '))

board = []
for _ in range(N):
    board.append(input())

c1 = 'BWBWBWBW'
c2 = 'WBWBWBWB'
pivot1 = [c1, c2, c1, c2, c1, c2, c1, c2]
pivot2 = [c2, c1, c2, c1, c2, c1, c2, c1]

ans = float('inf')
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for p in range(8):
            for q in range(8):
                if board[i+p][j+q] != pivot1[p][q]:
                    cnt1 += 1
                if board[i+p][j+q] != pivot2[p][q]:
                    cnt2 += 1
        ans = min(ans, cnt1, cnt2)

print(ans)