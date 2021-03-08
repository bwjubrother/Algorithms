import sys
sys.stdin = open('14501.txt', 'r')


def dp(pday, day, tp, profit):
    global max_profit
    if day > n:
        max_profit = max(max_profit, profit-tp[pday][1])
        return
    elif day == n:
        max_profit = max(max_profit, profit)
        return
    else:
        dp(day, day+tp[day][0], tp, profit+tp[day][1])
        dp(day, day+1, tp, profit)


n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
max_profit = 0
dp(0, 0, tp, 0)
print(max_profit)