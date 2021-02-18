import sys
sys.stdin = open('1149.txt', 'r')


N = int(input())
cr, cg, cb = map(int, input().split(' '))
for _ in range(1, N):
    r, g, b = map(int, input().split(' '))
    tmpr = r + min(cg, cb)
    tmpg = g + min(cr, cb)
    tmpb = b + min(cr, cg)
    cr, cg, cb = tmpr, tmpg, tmpb

print(min(cr, cg, cb))