import sys
sys.stdin = open('5204.txt', 'r')


def quickSort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr)
    print('#%d %d' % (tc+1, arr[n//2]))