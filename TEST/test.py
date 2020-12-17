import sys
sys.stdin = open('test1.txt', 'r')


def main(t):
    Ms, Ma = map(int, input().split())
    n, months = map(int, input().split())
    prices = [list(map(int, input().split())) for _ in range(n)]
    bought = [0] * n
    max_idx = -1
    budget = Ms

    for month in range(months + 1):
        price_diffs = [0] * n
        max_price = 0
        # 0개월 빼고 매달 입금
        if month > 0:
            budget += Ma
        # 매도
        for i in range(n):
            if bought[i]:
                budget += prices[i][month] * bought[i]
        bought = [0] * n
        # 차이 저장하기
        if month < months:
            for idx in range(n):
                price_diffs[idx] = prices[idx][month + 1] - prices[idx][month]
        # 자산 내로 매수
        max_price = max(price_diffs)
        max_idx = price_diffs.index(max(price_diffs))
        if max_price > 0:
            bought[max_idx] = budget // prices[max_idx][month]
            budget -= prices[max_idx][month] * bought[max_idx]
            price_diffs[max_idx] = 0
            max_price = max(price_diffs)
            max_idx = price_diffs.index(max(price_diffs))
            if (budget // prices[max_idx][month]) >= 1:
                bought[max_idx] = budget // prices[max_idx][month]
                budget -= prices[max_idx][month] * bought[max_idx]
        else:
            bought = [0] * n
            max_idx = -1

    ans = budget - (Ms + Ma * months)

    print('#%d %d' % (t + 1, ans))


if __name__ == "__main__":

    T = int(input())

    for t in range(T):
        main(t)
