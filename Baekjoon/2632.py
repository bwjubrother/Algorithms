import sys
sys.stdin = open('2632.txt', 'r')


order = int(input())
m, n = map(int, input().split())
a, b = [], []
for _ in range(m):
    a.append(int(input()))
for _ in range(n):
    b.append(int(input()))

a_comb = [0] * (sum(a)+1)
b_comb = [0] * (sum(b)+1)
a_comb[0], a_comb[-1] = 1, 1
b_comb[0], b_comb[-1] = 1, 1

for j in range(1, m):
    for i in range(m):
        if i+j > m:
            sum_a = sum(a[i:] + a[:(i+j)%m])
        else:
            sum_a = sum(a[i:i+j])
        a_comb[sum_a] += 1
for j in range(1, n):
    for i in range(n):
        if i+j > n:
            sum_b = sum(b[i:] + b[:(i+j)%n])
        else:
            sum_b = sum(b[i:i+j])
        b_comb[sum_b] += 1

answer = 0
for i in range(order+1):
    j = order-i
    if 0 <= i < len(a_comb) and 0 <= j < len(b_comb):
        answer += a_comb[i] * b_comb[j]
print(answer)

'''

from collections import deque
import sys
ipt = sys.stdin.readline


def init():
    total = int(ipt())
    m, n = map(int, ipt().split())
    a = [int(ipt()) for _ in range(m)]
    b = [int(ipt()) for _ in range(n)]
    return a, m, b, n, total
    

def get_count(a, m):
    count_a = [0] * (sum(a) + 1)
    count_a[0] = 1
    count_a[-1] = 1
    for i in range(m):
        q = deque(a)
        for _ in range(i):
            q.rotate(-1)
        q.pop()
        summ = 0
        while q:
            summ += q.popleft()
            count_a[summ] += 1
    return count_a


a, m, b, n, total = init()
count_a = get_count(a, m)
count_b = get_count(b, n)
answer = 0
for i in range(total + 1):
    j = total - i
    if 0 <= i < len(count_a) and 0 <= j < len(count_b):
        answer += count_a[i] * count_b[j]
print(answer)

'''