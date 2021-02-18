import sys
sys.stdin = open('9461.txt', 'r')

T = int(input())
memory = [1, 1, 1, 2, 2]
for _ in range(T):
    n = int(input())
    if n <= 5:
        print(memory[n-1])
    else:
        for _ in range(n-5):
            memory.append(memory[-1]+memory[-5])
        print(memory[n-1])