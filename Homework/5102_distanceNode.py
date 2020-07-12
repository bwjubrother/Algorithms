import sys
sys.stdin = open('5102.txt', 'r')


T = int(input())
for i in range(T):
    v, e = map(int, input().split())
    line = []
    for _ in range(e):
        line.append(list(map(int, input().split())))
    s, g = map(int, input().split())
    lines = [[0] * (v+1) for _ in range(v+1)]
    for j in line:
        lines[j[0]][j[1]] = 1
        lines[j[1]][j[0]] = 1
    visited = [0] * (v+1)
    distance = [0] * (v+1)
    queue = [s]
    ans = 0
    visited[s] = 1
    while queue:
        go = queue.pop(0)
        for next in range(1, v+1):
            if lines[go][next] and not visited[next]:
                queue.append(next)
                visited[next] = 1
                distance[next] = distance[go] + 1
                if next == g:
                    ans = distance[next]
                    break
    print('#%d %d' % (i+1, ans))


'''
T = int(input())
for i in range(T):
    v, e = map(int, input().split())
    line = []
    for _ in range(e):
        line.append(list(map(int, input().split())))
    s, g = map(int, input().split())
    lines = [[0] * (v+1) for _ in range(v+1)]
    for j in line:
        lines[j[0]][j[1]] = 1
        lines[j[1]][j[0]] = 1
    visited = [0] * (v+1)
    distance = [0] * (v+1)
    queue = [s]
    ans = 0
    while queue:
        go = queue.pop(0)
        if not visited[go]:
            visited[go] = 1
        for next in range(1, v+1):
            if lines[go][next] and not visited[next]:
                queue.append(next)
                distance[next] = distance[go] + 1
                if next == g:
                    ans = distance[next]
                    break
    print('#%d %d' %(i+1, ans))
'''