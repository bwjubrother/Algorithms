import sys
sys.stdin = open('5251.txt', 'r')

# ans : 2, 4, 10
T = int(input())
for tc in range(1, T+1):









'''
def short_path():
    key = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)
    check = set() # key 최소값 찾을 범위
    check.add(0)
    key[0] = 0
    while True:
        # key 최소값 찾기
        min_key = float('inf')
        s = -1
        for i in check:
            if key[i] < min_key:
                min_key = key[i]
                s = i

        # 확정
        visited[s] = True
        check.remove(s)
        if s == N:
            return key[s]

        # 다음 정점 key 갱신
        for e, w in link[s]:
            if key[e] > key[s] + w and not visited[e]:
                key[e] = key[s] + w
                check.add(e)


T = int(input())
for test_case in range(1, 1 + T):
    N, E = map(int, input().split())
    link = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s not in link:
            link[s] = [(e, w)]
        else:
            link[s] += [(e, w)]
    print('#{} {}'.format(test_case, short_path()))
'''