import sys
sys.stdin = open('5185.txt', 'r')


T = int(input())
for tc in range(T):
    n, ip = input().split()
    ans = ''
    for i in ip:
        hexnum = '0x' + i
        ans += format(int(hexnum, 16), '04b')
    print('#%d %s' % (tc+1, ans))