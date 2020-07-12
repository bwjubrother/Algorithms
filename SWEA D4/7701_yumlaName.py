import sys
sys.stdin = open('7701.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    names = []
    for i in range(n):
        names.append(str(input()))
    names = list(set(names))
    lenlist = []
    for name in names:
        lenlist.append([len(name), name])
    lenlist.sort()
    print('#%d' % (tc+1))
    for name in lenlist:
        print('%s' %(name[1]))