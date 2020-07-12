import sys
sys.stdin = open('5203.txt', 'r')


T = int(input())
for tc in range(T):
    ip = list(map(int, input().split()))
    acards, bcards = [], []
    aidx, bidx = [0] * 10, [0] * 10
    ans = 0
    for i in range(len(ip)):
        if i % 2:
            bcards.append(ip[i])
        else:
            acards.append(ip[i])
    for idx in range(len(acards)):
        aidx[acards[idx]] += 1
        bidx[bcards[idx]] += 1
        aidxsen = ''.join(list(map(str, aidx)))
        bidxsen = ''.join(list(map(str, bidx)))
        if '111' in aidxsen or '112' in aidxsen or '121' in aidxsen or '211' in aidxsen or 3 in aidx:
            ans = 1
            break
        if '111' in bidxsen or '112' in bidxsen or '121' in bidxsen or '211' in bidxsen or 3 in bidx:
            ans = 2
            break
    print('#%d %d' % (tc+1, ans))