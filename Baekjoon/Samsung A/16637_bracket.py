import sys

sys.stdin = open('16637.txt', 'r')

n = int(input())
inputs = input()





'''
#1
N = int(input())
expression = input()
answer = -2 ** 31
 
if N == 1:
    print(max(answer, int(expression)))
    exit()
 
symbol = ["+", "-", "*"]
 
 
def add_parenthesis(index, expression_list):
    global answer
    if index == N:
        for i, j in enumerate(expression_list):
            if len(j) == 3:
                expression_list[i] = str(eval(j))
        result = expression_list[0]
        for _ in range(1, len(expression_list), 2):
            result = eval(str(result)+expression_list[_]+expression_list[_+1])
 
        if answer < result:
            answer = result
        return
 
 
    expression_list.append(expression[index])
    add_parenthesis(index + 1, expression_list)
    del expression_list[-1]
 
    if expression_list[-1] in symbol and index + 3 <= N:
        expression_list.append(expression[index:index+3])
        add_parenthesis(index + 3, expression_list)
        del expression_list[-1]
 
 
add_parenthesis(1, [expression[0]])
print(answer)
'''

'''
#2
import sys
from collections import deque
from copy import deepcopy
read = sys.stdin.readline
maxAns = sys.maxsize * -1

def myCal(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '!':
        return num1

def case(check, depth):
    if depth == opNum:
        solve(check)
        return

    if depth > 0 and check[depth-1] == 1:
        check[depth] = 0
        case(check, depth+1)
    else:
        check[depth] = 0
        case(check, depth+1)
        check[depth] = 1
        case(check, depth+1)

def solve(check):
    global maxAns

    nums = deepcopy(originNums)
    ops = deepcopy(originOps)

    for i, c in enumerate(check):
        if c == 1:
            retVal = myCal(nums[i], ops[i], nums[i+1])
            nums[i] = retVal
            ops[i] = '!'
    #print(nums, ops)
    while ops:
        retVal = myCal(nums[0], ops[0], nums[1])
        nums.pop(1)
        nums[0] = retVal
        ops.pop(0)

    ans = nums[0]
    if ans > maxAns:
        maxAns = ans
    return

N = int(read())
calstr = read().replace('\n', '')

originNums = []
originOps = []
for i in range(N):
    if i%2 == 0:
        originNums.append(int(calstr[i]))
    else:
        originOps.append(calstr[i])

opNum = len(originOps)
case([0 for _ in range(opNum)], 0)
print(maxAns)
'''