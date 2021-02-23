import sys
sys.stdin = open('17137.txt', 'r')

DIV = 1000000007

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    cache = list(range(arr[-1]*n, 0, -n)) # [4, 3, 2, 1]
    for i in range(n-2, -1, -1):
        for j in range(arr[i] - 2, -1, -1):
            cache[j] = (cache[j] + cache[j+1]) 
    print(cache[0] % DIV)
