import sys
k, p, n = map(int, input().split(' '))
time = 0 
while time < n:
    k *= p
    time += 0.1
    print(time)

