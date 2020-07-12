import sys
sys.stdin = open('1248.txt', 'r')

# a로 부터 root까지의 거리
def distR(a):
    n = 1
    while parent[a] != 1:
        a = parent[a]
        n += 1
    return n

# a와 b의 공통조상 발견
def findP(a, b, a_d, b_d):
    if a_d > b_d:
        while a_d != b_d:
            a = parent[a]
            a_d -= 1
    else:
        while a_d != b_d:
            b = parent[b]
            b_d -= 1
    if a_d == b_d:
        while parent[a] != parent[b]:
            a = parent[a]
            b = parent[b]
    return parent[a]

# 공통조상의 모든 자손의 수
def findC(parent):
    m = 1
    for i in range(len(child[parent])):
        m += findC(child[parent][i])
    return m


T = int(input())
for tc in range(T):
    v, e, a, b = map(int, input().split())
    lis = list(map(int, input().split()))
    child = [[] for _ in range(v + 2)]
    parent = [0] * (v + 2)
    for i in range(0, e * 2, 2):
        parent[lis[i + 1]] = lis[i]
        child[lis[i]].append(lis[i + 1])
    a_d = distR(a)
    b_d = distR(b)
    prt = findP(a, b, a_d, b_d)
    cld = findC(prt)
    print('#%d %d %d' % (tc+1, prt, cld))