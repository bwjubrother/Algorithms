import sys
sys.stdin = open('9012.txt', 'r')

T = int(input())
for _ in range(T):
    ps = input()
    cnt = 0
    for p in ps:
        if p == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                print('NO')
                break
    if cnt > 0:
        print('NO')
        continue
    elif cnt < 0:
        continue
    else:
        print('YES')