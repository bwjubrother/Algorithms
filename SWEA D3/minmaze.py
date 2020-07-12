import sys

sys.stdin = open('minmaze.txt', 'r')


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())

for i in range(T):
    n = int(input())
    maze = [str(input()) for _ in range(n)]

    # 시작점 찾기
    for x in range(n):
        for y in range(n):
            if maze[x][y] == '2':
                sx = x
                sy = y

    # 탐색
    stack = []
    ans = []
    result = []
    visited = [[0] * n for _ in range(n)]
    stack.append((sx, sy))
    Rans = 0
    while len(stack) > 0:
        s = stack.pop()
        if visited[s[0]][s[1]] != 1:
            visited[s[0]][s[1]] == 1

        for j in range(4):
            if maze[s[0] + delta[j][0]][s[1] + delta[j][1]] == '0' and visited[s[0] + delta[j][0]][s[1] + delta[j][1]] == 0:
                stack.append((s[0] + delta[j][0], s[1] + delta[j][1]))
                result.append((s[0] + delta[j][0], s[1] + delta[j][1]))
            elif maze[s[0] + delta[j][0]][s[1] + delta[j][1]] == '3':
                ans.append(len(result))
                result = []
            else:
                Rans = -1
                break
        if Rans == -1:
            break
    print(result)
    print(Rans)