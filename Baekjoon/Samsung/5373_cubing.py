import sys
sys.stdin = open('5373.txt', 'r')


n = int(input())
for _ in range(n):
    num = int(input())
    rotates = list(input().split(' '))
