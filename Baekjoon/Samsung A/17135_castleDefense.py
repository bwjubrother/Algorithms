import sys

sys.stdin = open('17135.txt')

N, M, D = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))
    
print(board)