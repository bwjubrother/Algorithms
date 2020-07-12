import sys

sys.stdin = open('1234.txt', 'r')

for i in range(10):
    num, sen = input().split()
    num = int(num)
    while True:
        init = sen
        for idx, j in enumerate(sen):
            if idx == 0:
                continue
            elif j == sen[idx-1]:
                sen = sen.replace(sen[idx-1:idx+1], '')
                break
        if init == sen:
            break
    print('#%d %s' %(i+1, sen))
