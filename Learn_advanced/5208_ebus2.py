import sys
sys.stdin = open('5208.txt', 'r')

def DFS(num):
    global cnt, result

    if num >= N:
        if result > cnt:
            result = cnt
        return

    if result < cnt:
        return

    start = num
    life = Data[start]

    for i in range(start+life, start, -1):
        cnt += 1
        DFS(i)
        cnt -= 1


TC = int(input())
for tc in range(1,TC+1):
    Data = list(map(int, input().split()))
    N = Data[0]
    result = 987654321
    cnt = 0

    DFS(1)

    print('#%d %d'%(tc, result-1))