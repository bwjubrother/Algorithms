import sys

sys.stdin = open('5656.txt', 'r')

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def drop(k, n, w, h):
    global minleft
    if k == n:
        left = breakbrick(w, h)
        if minleft > left:
            minleft = left
    else:
        for i in range(w):
            idx.append(i)
            drop(k+1, n, w, h)

def breakbrick(w, h):
    q = []
    for i in range(n):
        for j in range(h):
            if board[j][idx[i]]:
                q.append((j, idx[i]))
                break




T = int(input())
for i in range(T):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    idx = []
    minleft = float('inf')
    drop(0, n, w, h)