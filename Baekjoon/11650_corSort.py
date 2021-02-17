import sys
sys.stdin = open('11650.txt', 'r')

N = int(input())
cors = []
for _ in range(N):
    cors.append(list(map(int, input().split(' '))))

cors.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(' '.join(map(str, cors[i])))
