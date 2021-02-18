N = input()
minN = int(N) - len(N) * 9
if minN < 0:
    minN = 0
for i in range(minN, int(N)):
    if (i + sum(list(map(int, str(i))))) == int(N):
        print(i)
        break
else:
    print(0)