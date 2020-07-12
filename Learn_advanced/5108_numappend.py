import sys
sys.stdin = open('5108.txt', 'r')


T = int(input())

for i in range(T):
    n, m, l = map(int, input().split())
    numlist = input().split()
    for j in range(m):
        ans = []
        idx, num = map(int, input().split())
        ans += numlist[:idx]
        ans.append(str(num))
        ans += numlist[idx:]
        numlist = ans
    print('#%d %s' % (i+1, ans[l]))