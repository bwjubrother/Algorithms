def dfs(last, level, covered_count):
    global min_AP
    # 모든 기기가 커버되면 level과 min_AP 비교
    if covered_count >= len(machines):
        if min_AP > level:
            min_AP = level
    # 기기가 5개 이상이면 종료
    if level >= 5:
        return
    for i in range(last + 1, len(ports)):
        if used_port[i]:
            continue
        used_port[i] = 1
        r, c = ports[i]
        checked = []
        for j, m in enumerate(machines):
            if covered_machine[j] == 1:
                continue
            mr, mc, dist = m
            if abs(mr - r) + abs(mc - c) <= R + dist:
                covered_machine[j] = 1
                checked.append(j)
        dfs(i, level + 1, covered_count + len(checked))
        used_port[i] = 0
        for j in checked:
            covered_machine[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ports = []
    machines = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                ports.append((r, c))
            elif 1 <= board[r][c] <= 3:
                machines.append((r, c, board[r][c]))

    used_port = [0] * len(ports)
    covered_machine = [0] * len(machines)
    min_AP = float('inf')
    dfs(-1, 0, 0)
    if min_AP == float('inf'):
        min_AP = -1
    print('#%d %d' % (tc, min_AP))