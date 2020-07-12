import sys
sys.stdin = open('3378.txt', 'r')


T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    stylish = [input() for _ in range(p)]
    me = [input() for _ in range(q)]
    c1, c2, c3, c4, c5, c6 = 0, 0, 0, 0, 0, 0
    a, b, c, d, e, f, g = 0, 0, 0, 0, 0, 0, 0
    for idx, sen in enumerate(stylish):
        c1 += sen.count('(')
        c2 += sen.count(')')
        c3 += sen.count('{')
        c4 += sen.count('}')
        c5 += sen.count('[')
        c6 += sen.count(']')
        c12 = c1-c2
        c34 = c3-c4
        c56 = c5-c6
        if c12 and c34 and c56:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    a = idx2+1
                    break
        elif c12 and c34:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    b = idx2 + 1
                    break
        elif c34 and c56:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    c = idx2 + 1
                    break
        elif c12 and c56:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    d = idx2 + 1
                    break
        elif c12:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    e = idx2 + 1
                    break
        elif c34:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    f = idx2 + 1
                    break
        elif c56:
            for idx2, dot in enumerate(stylish[idx + 1]):
                if dot != '.':
                    g = idx2 + 1
                    break
    ans = [0]
    for sen in me[:-1]:
        if '(' in sen:
            ans.append(e)
        if '{' in sen:
            ans.append(f)
        if '[' in sen:
            ans.append(g)
    print(ans)


'''
for T in range(1,int(input())+1):
    p,q=map(int,input().split())
    a,b=[input() for i in range(p)],[input() for i in range(q)]
 
    dic = {}
    r=c=s=0
    li = []
    for i in range(len(a)):
        j=0
        while j < len(a[i]) and a[i][j] =='.':j+=1
        li += [(r,c,s,j)]
        dic[(r,c,s)] = j
        while j < len(a[i]):
            if a[i][j]=='(':r+=1
            if a[i][j]==')':r-=1
            if a[i][j]=='{':c+=1
            if a[i][j]=='}':c-=1
            if a[i][j]=='[':s+=1
            if a[i][j]==']':s-=1
            j+=1
 
    rcs = [[i,j,k] for i in range(1,21) for j in range(1,21) for k in range(1,21)]
    newrcs = []
    while rcs:
        R,C,S = rcs[-1]
        flag = True
        for r,c,s,cnt in li:            
            if r*R + c*C + s*S != cnt:
                flag = False
                break
        if flag:
            newrcs += [(R,C,S)]
        rcs.pop()
     
    R,C,S=newrcs[0]
    for r,c,s in newrcs[1:]:
        if R != r: R = -1
        if C != c: C = -1
        if S != s: S = -1
     
    res = []
    r=c=s=0
    for i in range(len(b)):
        if (r,c,s) in dic:
            res += [dic[(r,c,s)]]
        elif (R == -1 and r != 0) or (C == -1 and c != 0) or (S == -1 and s != 0):            
            res += [-1]
        else:
            res += [R*r + C*c + S*s]
 
        j=0
        while j < len(b[i]):
            if b[i][j]=='(':r+=1
            if b[i][j]==')':r-=1
            if b[i][j]=='{':c+=1
            if b[i][j]=='}':c-=1
            if b[i][j]=='[':s+=1
            if b[i][j]==']':s-=1
            j+=1
 
    print('#%d' %T, *res)

'''