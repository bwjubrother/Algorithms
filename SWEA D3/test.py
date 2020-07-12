import sys
sys.stdin = open('5656.txt', 'r')

T = int(input())
for i in range(T):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(w)]
    board = list(map(list, zip(*board)))
    print(board)