import sys
sys.stdin = open('6206.txt', 'r')

# 1 30 322494480
T = int(input())
for tc in range(T):
    m, n = map(int, input().split())
    ans = m ** n
    for i in range(m-1, 1, -1):
        ans -= i ** n
    print(ans)
