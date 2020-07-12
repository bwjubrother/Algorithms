import sys
sys.stdin = open('14889.txt', 'r')


N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
