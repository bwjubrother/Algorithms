import sys

sys.stdin = open('5986.txt', 'r')


T = int(input())
for i in range(T):
    n = int(input())
    a = [False, False] + [True] * (n - 1)
    primes = []
    ans = 0
    for j in range(2, n + 1):
        if a[j]:
            primes.append(j)
            for k in range(2 * j, n + 1, j):
                a[k] = False
    for x in range(len(primes)):
        for y in range(x, len(primes)):
            for z in range(y, len(primes)):
                if primes[x] + primes[y] + primes[z] == n:
                    ans += 1
    print('#%d %d' %(i+1, ans))