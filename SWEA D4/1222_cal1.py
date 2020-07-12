import sys
sys.stdin = open('1222.txt', 'r')


for tc in range(10):
    n = int(input())
    formula = str(input())
    stack = []
    ans = 0
    for i in range(n):
        if not i % 2:
            ans += int(formula[i])
    print('#%d %d' % (tc+1, ans))
