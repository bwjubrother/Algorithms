import sys
sys.stdin = open('5432.txt', 'r')


T = int(input())
for tc in range(T):
    ip = input()
    ans = 0
    stick = 0
    for i in range(len(ip)):
        if ip[i] == '(':
            stick += 1
            if ip[i+1] == ')':
                stick -= 1
                ans += stick
        if ip[i] == ')' and ip[i-1] != '(':
            stick -= 1
            ans += 1
    print('#%d %d' % (tc+1, ans))