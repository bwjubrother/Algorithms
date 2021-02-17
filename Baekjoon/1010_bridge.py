import sys
sys.stdin = open('1010.txt', 'r')

def facto(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * facto(n-1)

def comb(n, r):
    return facto(n) // (facto(r) * facto(n-r))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '))
    print(comb(M, N))