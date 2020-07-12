import sys
sys.stdin = open('3143.txt', 'r')


T = int(input())
for tc in range(T):
    a, b = input().split()
    ans = len(a) - a.count(b)*(len(b)-1)
    print('#%d %d' %(tc+1, ans))