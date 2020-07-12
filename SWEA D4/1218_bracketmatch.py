import sys
sys.stdin = open('1218.txt', 'r')


openb = ['(', '[', '{']

for tc in range(1, 11):
    n = int(input())
    ip = input()
    stack = []
    ans = 1
    for i in ip:
        if i in openb:
            stack.append(i)
        else:
            if i == ')' and stack.pop() != '(':
                ans = 0
                break
            if i == '}' and stack.pop() != '{':
                ans = 0
                break
            if i == ']' and stack.pop() != '[':
                ans = 0
                break
    if stack:
        ans = 0
    print('#%d %d' % (tc, ans))