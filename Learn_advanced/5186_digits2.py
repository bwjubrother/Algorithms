import sys
sys.stdin = open('5186.txt', 'r')


T = int(input())
for tc in range(T):
    ip = float(input())
    ans = ''
    digit = 1
    for i in range(13):
        digit = float(digit / 2)
        if ip >= digit:
            ip -= digit
            ans += '1'
        else:
            ans += '0'
        if ip == 0:
            break
        if i == 12:
            ans = 'overflow'
    print('#%d %s' % (tc+1, ans))