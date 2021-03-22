import sys
sys.stdin = open('17406.txt', 'r')


from itertools import permutations
from copy import deepcopy

# 회전 - 50*50=2500
def rotate(_cube, r, c, s):
    for i in range(1, s+1):
        tmp = _cube[r-i][c-i]
        for k in range(-i, i):
            _cube[r+k][c-i] = _cube[r+k+1][c-i]
        for k in range(-i, i):
            _cube[r+i][c+k] = _cube[r+i][c+k+1]
        for k in range(i, -i, -1):
            _cube[r+k][c+i] = _cube[r+k-1][c+i]
        for k in range(i, -i+1, -1):
            _cube[r-i][c+k] = _cube[r-i][c+k-1]
        _cube[r-i][c-i+1] = tmp
    return _cube
 

n, m, k = map(int, input().split())
cube = [list(map(int, input().split())) for _ in range(n)]
acts = [list(map(int, input().split())) for _ in range(k)]


# 회전 순서 (순열) - k!(6!=720)
min_res = float('inf')
for perm in permutations(acts, k):
    min_sum = float('inf')
    _cube = deepcopy(cube)
    for item in perm:
        r, c, s = item
        _cube = rotate(_cube, r-1, c-1, s)
    # 행의 합 - n
    for row in _cube:
        min_sum = min(min_sum, sum(row))
    min_res = min(min_res, min_sum)

print(min_res)

