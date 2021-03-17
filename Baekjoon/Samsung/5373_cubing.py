import sys
sys.stdin = open('5373.txt', 'r')


'''
### 복잡해서 포기.

def rotate(plane, direction):
    global ceil, floor, front, back, left, right
    if direction == '+':
        if plane == 'L':
            left = list(map(list, zip(*left[::-1])))
            for i in range(3):
                tmp = ceil[i][0]
                ceil[i][0] = back[i][0]
                back[i][0] = floor[i][0]
                floor[i][0] = front[i][0]
                front[i][0] = tmp 
        elif plane == 'R':
            right = list(map(list, zip(*right[::-1])))
            for i in range(3):
                tmp = ceil[i][2]
                ceil[i][2] = front[i][2]
                front[i][2] = floor[i][2]
                floor[i][2] = back[i][2]
                back[i][2] = tmp   
        elif plane == 'U':
            ceil = list(map(list, zip(*ceil[::-1])))
            for i in range(3):
                tmp = front[i][0]
                front[i][0] = right[i][0]
                right[i][0] = back[-i-1][0]
                back[-i-1][0] = right[-i-1][0]
                front[i][0] = tmp    

    elif direction == '-':
        if plane == 'L':
            left = list(map(list, zip(*left)))[::-1]
            for i in range(3):
                tmp = ceil[i][0]
                ceil[i][0] = front[i][0]
                front[i][0] = floor[i][0]
                floor[i][0] = back[i][0]
                back[i][0] = tmp
        elif plane == 'R':
            right = list(map(list, zip(*right)))[::-1]
            for i in range(3):
                tmp = ceil[i][2]
                ceil[i][2] = back[i][2]
                back[i][2] = floor[i][2]
                floor[i][2] = front[i][2]
                front[i][2] = tmp


# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다. 
# 두 번째 문자는 돌린 방향이다. +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향
t = int(input())
for _ in range(t):
    # 위 흰색, 아래 노란색, 앞 빨간, 뒤 오렌지, 왼 초록, 오른 파랑
    ceil = [['w'] * 3 for _ in range(3)]
    floor = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

    n = int(input())
    rotates = list(input().split(' '))
    for item in rotates:
        rotate(item[0], item[1])
    for row in ceil:
        print(''.join(row))
        
'''

# 정답 풀이
import sys
input = sys.stdin.readline
def rotate(color, ro):
    if ro == "-":
        temp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                temp[2 - j][i] = color[i][j]
        return temp
    else:
        temp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                temp[j][2 - i] = color[i][j]
        return temp
def rotation(p, ro):
    global w, y, r, o, g, b
    if p == "U":
        if ro == "-":
            r1, r2, r3, b1, b2, b3 = r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2]
            o1, o2, o3, g1, g2, g3 = o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2]
            r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2] = g1, g2, g3, r1, r2, r3
            o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2] = b1, b2, b3, o1, o2, o3
            w = rotate(w, ro)
        else:
            r1, r2, r3, b1, b2, b3 = r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2]
            o1, o2, o3, g1, g2, g3 = o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2]
            r[0][0], r[0][1], r[0][2], b[0][0], b[0][1], b[0][2] = b1, b2, b3, o1, o2, o3
            o[0][0], o[0][1], o[0][2], g[0][0], g[0][1], g[0][2] = g1, g2, g3, r1, r2, r3
            w = rotate(w, ro)
    elif p == "D":
        if ro == "-":
            r1, r2, r3, b1, b2, b3 = r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2]
            o1, o2, o3, g1, g2, g3 = o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2]
            r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2] = b1, b2, b3, o1, o2, o3
            o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2] = g1, g2, g3, r1, r2, r3
            y = rotate(y, ro)
        else:
            r1, r2, r3, b1, b2, b3 = r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2]
            o1, o2, o3, g1, g2, g3 = o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2]
            r[2][0], r[2][1], r[2][2], b[2][0], b[2][1], b[2][2] = g1, g2, g3, r1, r2, r3
            o[2][0], o[2][1], o[2][2], g[2][0], g[2][1], g[2][2] = b1, b2, b3, o1, o2, o3
            y = rotate(y, ro)
    elif p == "F":
        if ro == "-":
            y1, y2, y3, w1, w2, w3 = y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2]
            b1, b2, b3, g1, g2, g3 = b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2]
            y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2] = g1, g2, g3, b1, b2, b3
            b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2] = y3, y2, y1, w3, w2, w1
            r = rotate(r, ro)
        else:
            y1, y2, y3, w1, w2, w3 = y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2]
            b1, b2, b3, g1, g2, g3 = b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2]
            y[0][0], y[0][1], y[0][2], w[2][0], w[2][1], w[2][2] = b3, b2, b1, g3, g2, g1
            b[0][0], b[1][0], b[2][0], g[0][2], g[1][2], g[2][2] = w1, w2, w3, y1, y2, y3
            r = rotate(r, ro)
    elif p == "B":
        if ro == "-":
            w1, w2, w3, b1, b2, b3 = w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2]
            g1, g2, g3, y1, y2, y3 = g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2]
            w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2] = g3, g2, g1, w1, w2, w3
            g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2] = y1, y2, y3, b3, b2, b1
            o = rotate(o, ro)
        else:
            w1, w2, w3, b1, b2, b3 = w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2]
            g1, g2, g3, y1, y2, y3 = g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2]
            w[0][0], w[0][1], w[0][2], b[0][2], b[1][2], b[2][2] = b1, b2, b3, y3, y2, y1
            g[0][0], g[1][0], g[2][0], y[2][0], y[2][1], y[2][2] = w3, w2, w1, g1, g2, g3
            o = rotate(o, ro)
    elif p == "L":
        if ro == "-":
            w1, w2, w3, r1, r2, r3 = w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0]
            y1, y2, y3, o1, o2, o3 = y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0] = r1, r2, r3, y1, y2, y3
            y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = o3, o2, o1, w3, w2, w1
            g = rotate(g, ro)
        else:
            w1, w2, w3, r1, r2, r3 = w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0]
            y1, y2, y3, o1, o2, o3 = y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2]
            w[0][0], w[1][0], w[2][0], r[0][0], r[1][0], r[2][0] = o3, o2, o1, w1, w2, w3
            y[0][0], y[1][0], y[2][0], o[0][2], o[1][2], o[2][2] = r1, r2, r3, y3, y2, y1
            g = rotate(g, ro)
    elif p == "R":
        if ro == "-":
            w1, w2, w3, r1, r2, r3 = w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2]
            y1, y2, y3, o1, o2, o3 = y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2] = o3, o2, o1, w1, w2, w3
            y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = r1, r2, r3, y3, y2, y1
            b = rotate(b, ro)
        else:
            w1, w2, w3, r1, r2, r3 = w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2]
            y1, y2, y3, o1, o2, o3 = y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0]
            w[0][2], w[1][2], w[2][2], r[0][2], r[1][2], r[2][2] = r1, r2, r3, y1, y2, y3
            y[0][2], y[1][2], y[2][2], o[0][0], o[1][0], o[2][0] = o3, o2, o1, w3, w2, w1
            b = rotate(b, ro)
t = int(input())
for i in range(t):
    w = [["w"] * 3 for i in range(3)]
    y = [["y"] * 3 for i in range(3)]
    r = [["r"] * 3 for i in range(3)]
    o = [["o"] * 3 for i in range(3)]
    g = [["g"] * 3 for i in range(3)]
    b = [["b"] * 3 for i in range(3)]
    n = int(input())
    s = input().split()
    for i in s:
        p, ro = list(i)
        rotation(p, ro)
    for i in range(3):
        print(''.join(w[i]))