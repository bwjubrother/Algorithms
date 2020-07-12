import sys
sys.stdin = open('1486.txt', 'r')


T = int(input())
for i in range(T):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    check = [0] * 200001
    sumh = 0
    for h in heights:
        for j in range(sumh, -1, -1):
            if check[j]:
                check[j+h] = 1
        sumh += h
        check[h] = 1
    for k in range(b, sumh+1):
        if check[k]:
            break
    print('#%d %d' % (i+1, k - b))


'''
T = int(input())
for i in range(T):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort(reverse = True)
    sumh = 0
    difflist = []
    for h in heights:
        sumh += h
        if sumh >= b:
            difflist.append(sumh-b)  #78988
            sumh -= h
            break
    print(heights[::-1])
    sumh += heights[-1]
    print(sumh)
    # print('#%d %d' %(i+1, min(difflist)))
'''