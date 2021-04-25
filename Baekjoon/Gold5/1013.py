import sys
sys.stdin = open('./1013.txt', 'r')


import re


t = int(input())
for _ in range(t):
    # target (100+1+ | 01)+
    record = str(input())
    target = re.compile('(100+1+|01)+')
    if target.fullmatch(record):
        print('YES')
    else:
        print('NO')