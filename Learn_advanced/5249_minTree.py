'''
Prim 알고리즘

V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s][e] = c
    adj[e][s] = c
# for row in adj:
#   print(row)

# key, p, mst 준비
INF = float('inf')
key = [INF] * V  # 가중치
p = [-1] * V  # 부모노드
mst = [False] * V  # 방문기록


key[0] = 0
cnt = 0
while cnt < V:
    for i in range(V):
        min = INF
        u = -1
        for i in range(V):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i

        mst[u] = True
        result += min
        cnt += 1

        for w in range(V):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u

print(result)

'''

'''
Prim (인접리스트)

V, E = map(int, input().split())
adj = {i : [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])
    
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []

key[0] = 0

heapq.heappush(pq,(0,0)) 

while pq:
    k, node = heapq.heappop(pq)
    mst[node] = True
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            heapq.heappush(pq,(key[dest],dest))
'''

import sys
sys.stdin = open('5249.txt', 'r')


def Prim(G, s):
    key = [float('inf')] * (V+1)
    pi = [None] * (V+1)
    visited = [False] * (V+1)
    key[s] = 0

    for _ in range(V+1):
        minIdx = -1
        min = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] < min:
                min = key[i]
                minIdx = i
        visited[minIdx] = True
        for node, val in G[minIdx]:
            if not visited[node] and val < key[node]:
                key[node] = val
                pi[node] = minIdx
    return sum(key)


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end, val = map(int, input().split())
        Graph[start].append((end, val))
        Graph[end].append((start, val))
    print('#%d %d' % (tc+1, Prim(Graph, 0)))