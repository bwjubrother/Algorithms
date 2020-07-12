import sys

sys.stdin = open('1230.txt', 'r')


for i in range(1):
    N = int(input())
    init = list(map(str, input().split()))
    M = int(input())
    Ms = list(map(str, input().split()))

    for idx, j in enumerate(Ms):
        if j == 'I':
            location = int(Ms[idx+1])
            num = int(Ms[idx+2])
            init = init[:location] + Ms[idx+3:idx+3+num] + init[location:]
        elif j == 'D':
            location = int(Ms[idx+1])
            num = int(Ms[idx+2])
            for k in range(num):
                init.pop(location)
        elif j == 'A':
            num = int(Ms[idx + 1])
            init = init + Ms[idx+2:idx+2+num]
            
    print('#%d %s' %(i+1, ' '.join(init)))


