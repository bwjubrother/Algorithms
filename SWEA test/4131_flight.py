import sys
sys.stdin = open('4131.txt', 'r')


def find(road):
    slope = [False] * n
    for idx in range(n):


T = int(input())
for tc in range(T):
    n, x = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(n)]
