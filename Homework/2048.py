import sys

sys.stdin = open('input1.txt', 'r')


def play(numbers):
    for line in numbers:
        zerocount = 0
        for zero in line:
            if zero == 0:
                zerocount += 1
        for _ in range(zerocount):
            line.remove(0)
        print(line)
        for idx, l in enumerate(line):
            if idx == 0:
                continue
            else:
                if l == line[idx-1]:
                    line[idx-1] = 2 * l
                    line[idx] = -1
    for line in numbers:
        for minus in line:
            if minus == -1:
                line.remove(-1)
    for line in numbers:
        for z in range(N-len(line)):
            line.append(0)
    return numbers




num = int(input())

for i in range(num):
    N, S = input().split()
    N = int(N)

    numbers = [list(map(int, input().split())) for _ in range(N)]
    newnumbers = []
    ans = []

    if S == 'up':
        numbers = list(zip(*numbers))
        for j in numbers:
            newnumbers.append(list(j))
        numbers = play(newnumbers)
        numbers = list(zip(*numbers))
        for j in numbers:
            ans.append(list(j))

    if S == 'down':
        numbers = list(zip(*numbers))
        reverse = []
        for j in numbers:
            newnumbers.append(list(j)[::-1])
        numbers = play(newnumbers)
        for j in numbers:
            reverse.append(list(j)[::-1])
        numbers = list(zip(*reverse))
        for j in numbers:
            ans.append(list(j))

    if S == 'left':
        ans = play(numbers)


    if S == 'right':
        for j in numbers:
            newnumbers.append(list(j)[::-1])
        numbers = play(newnumbers)
        for j in numbers:
            ans.append(list(j)[::-1])

    print("#%d" %(i+1))
    for p in ans:
        print(' '.join(list(map(str,p))))