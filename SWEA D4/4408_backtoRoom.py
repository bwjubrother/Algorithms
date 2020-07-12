import sys
sys.stdin = open('4408.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    rooms = [0] * 401
    for i in range(n):
        start, end = map(int, input().split())
        if start <= end:
            if not start % 2:
                start -= 1
            if end % 2:
                end += 1
            for idx in range(start, end+1):
                rooms[idx] += 1
        else:
            if not end % 2:
                end -= 1
            if start % 2:
                start += 1
            for idx in range(end, start+1):
                rooms[idx] += 1
    print('#%d %d' % (tc+1, max(rooms)))