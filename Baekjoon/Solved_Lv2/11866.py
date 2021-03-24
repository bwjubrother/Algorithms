from collections import deque


n, k = map(int, input().split())
stack = deque([i for i in range(1, n+1)])
idx = -1
res = []
while stack:
    for _ in range(k-1):
        stack.append(stack.popleft())
    res.append(str(stack.popleft()))
print('<' + ', '.join(res) + '>')
