import sys
sys.stdin = open('1874.txt', 'r')


n = int(input())

stack = []
num = 1
res = []
for _ in range(n):
    inp = int(input())
    while num <= inp:
        stack.append(num)
        res.append('+')
        num += 1
    if inp != stack.pop():
        break
    else:
        res.append('-')

if stack:
    print('NO')
else:
    for item in res:
        print(item)