import sys
sys.stdin = open('5099.txt', 'r')


T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    stack = []
    for j in range(n):
        stack.append([j+1, pizza[j]])

    idx = 0
    while len(stack) != 1:
        stack[0][1] //= 2
        if not stack[0][1]:
            if n+idx < m:
                stack.pop(0)
                stack.append([n+idx+1, pizza[n+idx]])
                idx += 1
            else:
                stack.pop(0)
        else:
            stack.append(stack.pop(0))
    print('#%d %d' %(i+1, stack[0][0]))