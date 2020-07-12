import sys
sys.stdin = open('2.txt', 'r')


dx = [0, 1, 1, 1, 0, -1, -1, -1]  #8방향 탐색
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def inside(x, y): #인덱스아웃을 방지하는 함수
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

T = int(input())
for tc in range(T):
    n = int(input())
    land = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)] #방문기록을 남기기위한 같은 크기의 2차원 배열
    anslist = [] #광물 영역에 따른 광물량과 크기를 저장하기 위한 리스트
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and land[x][y]: #방문하지 않았고 광물이 0이 아니면
                stack = [(x, y)] #스택에 그 위치를 저장
                scale = 1
                while stack: #스택이 남아있을 때까지
                    nx, ny = stack.pop()
                    visited[nx][ny] = 1
                    for i in range(8): #8방향 탐색
                        newx = nx + dx[i]
                        newy = ny + dy[i]
                        if inside(newx, newy) and not visited[newx][newy] and land[newx][newy] == land[x][y]: # 인덱스 아웃이 아니고 방문하지 않았고 광물의 종류가 같다면
                            stack.append((newx, newy)) #위치 추가
                            visited[newx][newy] = 1 #방문기록
                            scale += 1 #크기 +1
                amount = scale * land[x][y] #광물양은 크기 * 광물종류
                anslist.append([amount, scale])
    anslist = sorted(anslist, reverse=True) #광물양의 크기가 큰 순서대로 정렬
    max_amount = anslist[0][0]
    min_scale = anslist[0][1]
    for ans in anslist:
        if ans[0] == max_amount and ans[1] < min_scale: #광물양이 젤 크면서 면적이 젤 작은 값을 탐색
            min_scale = ans[1]
    print('#%d %d %d' % (tc+1, max_amount, min_scale))