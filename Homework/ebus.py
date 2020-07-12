import sys

sys.stdin = open("input.txt", "r")

num = int(input())

for n in range(num):
    case = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    bus = 0
    count = 0
    while bus < case[1]:
        wrong = case[0]
        for i in range(bus + case[0], bus, -1):
            bus = i
            if bus >= case[1]:
                break
            elif bus in stops:
                count += 1
                break
            wrong -= 1
            if wrong == 0:
                count = 0
                bus = case[1]
                break
    print('#%d %d' %(n+1, count))

