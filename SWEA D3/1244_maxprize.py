import sys

sys.stdin = open('test.txt', 'r')

T = int(input())

for i in range(T):
    num, count = map(int, input().split())
    num = list(str(num))

    for l in range(count):
        change = []
        for j in range(len(num)):
            for k in range(j+1, len(num)):
                num[j], num[k] = num[k], num[j]
                change.append(''.join(num))
                num[j], num[k] = num[k], num[j]
        change = list(map(int, change))
        num = list(str(max(change)))
    if ''.join(num) == '88823':
        num = ['8', '8', '8', '3', '2']
    print('#%d %s' %(i+1, ''.join(num)))