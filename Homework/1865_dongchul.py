import sys
sys.stdin = open('1865.txt', 'r')


def perm(k, mulP):
    global maxP
    if mulP <= maxP:
        return
    if k == n:
        maxP = mulP
        return
    for i in range(n):
        if not idx[i]:
            idx[i] = 1
            perm(k+1, mulP * Ps[k][i]/100)
            idx[i] = 0

T = int(input())
for tc in range(T):
    n = int(input())
    Ps = [list(map(int, input().split())) for _ in range(n)]
    idx = [0] * n
    maxP = 0
    perm(0, 1)
    print('#%d %.6f' % (tc+1, maxP * 100))





'''
def perm(idx, k, mulP):
    global maxP
    if mulP <= maxP:
        return
    if k == n:
        maxP = mulP
    else:
        for i in range(k, n):
            idx[k], idx[i] = idx[i], idx[k]
            perm(idx, k+1, mulP * Ps[k][i])
            idx[k], idx[i] = idx[i], idx[k]


T = int(input())
for tc in range(T):
    n = int(input())
    Ps = [list(map(int, input().split())) for _ in range(n)]
    idx = [i for i in range(n)]
    maxP = 0
    perm(idx, 0, 1)
    print('#%d %.6f' % (tc+1, maxP * 100))
'''