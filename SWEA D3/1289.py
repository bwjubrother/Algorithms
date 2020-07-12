import sys

sys.stdin = open('1289.txt', 'r')


T = int(input())

for i in range(T):
    num = str(input())
    ans = 0
    status = '1'
    for idx, j in enumerate(num):
        if idx == 0:
            if j == '1':
                ans += 1
            else:
                continue
        elif j != num[idx-1]:
            ans += 1
    print('#%d %d' % (i + 1, ans))
