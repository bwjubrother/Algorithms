import sys
sys.stdin = open('12865.txt', 'r')

'''
def packing(idx, weight, value):
    global max_value
    if idx == n:
        max_value = max(max_value, value)
        return
    if weight+items[idx][0] > k:
        max_value = max(max_value, value)
        return   
    else:
        packing(idx+1, weight+items[idx][0], value+items[idx][1])
        packing(idx+1, weight, value)

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

max_value = 0
packing(0, 0, 0)
print(max_value)
'''

n, k = map(int, input().split())
weights = [0] * (k+1)
for _ in range(n):
    w, v = map(int, input().split())
    if w > k:
        continue
    for i in range(k, 0, -1):
        if weights[i] and i + w <= k:
            weights[i+w] = max(weights[i+w], weights[i]+v)
    weights[w] = max(weights[w], v)

print(max(weights))
