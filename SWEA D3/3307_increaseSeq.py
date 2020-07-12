import sys

sys.stdin = open('3307.txt', 'r')

def find(x):
    global ans
    for next in seq[x+1:]:


for i in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    ans = 0
    for idx in range(len(seq)):
        find(idx)
