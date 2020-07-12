import sys
sys.stdin = open('5204.txt', 'r')


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = mergeSort(arr)
    mid = arr[n//2]
    print('#%d %d %d' % (tc+1, mid, cnt))