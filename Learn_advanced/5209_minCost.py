import sys
sys.stdin = open('5209.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    