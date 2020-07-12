import sys
sys.stdin = open('1868.txt', 'r')

#가장 교차점이 많은 노드 찾기
def maxCross(node):
    maxcross, maxnode = 0, 0
    for idx, no in enumerate(node):
        if len(no) > maxcross:
            maxcross = len(no)
            maxnode = idx
    return maxnode


n = int(input())
node = [[] for _ in range(n+1)]
# 간선 저장
for _ in range(n-1):
    a, b = map(int, input().split())
    node[b].append(a)
    node[a].append(b)
cnt = 0
# 플레이
while True:
    topnode = maxCross(node)
    if topnode:
        node.pop(topnode)
        for no in node:
            if topnode in no:
                no.remove(topnode)
        cnt += 1
    else:
        break
print(cnt)

