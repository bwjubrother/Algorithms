import sys
sys.stdin = open('17124.txt', 'r')

'''
# 1 무식하게 풀기 (n * m)
T = int(input())
for _ in range(T):
    n, m = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    ans = 0
    for a in A:
        minDiff, minNum = float('inf'), float('inf')
        for b in B:
            if (abs(a - b) == minDiff and b < minNum) or (abs(a - b) < minDiff) :
                minNum = b
                minDiff = abs(a - b)
        ans += minNum
    print(ans)
'''

# 2 이진탐색 (n * log(n))
def binSearch(goal, arr, start, end):
    diff = end - start
    if diff <= 1:
        return start
    mid = (start + end) // 2
    if goal < arr[mid]:
        return binSearch(goal, arr, start, mid)
    else:
        return binSearch(goal, arr, mid, end)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    B.sort()
    ans = 0
    for a in A:
        find = binSearch(a, B, 0, m)
        findlist = []
        for i in range(-1, 2):
            findlist.append(abs(B[(find+i) % m] - a))
        ans += B[findlist.index(min(findlist)) + find - 1]
    print(ans)