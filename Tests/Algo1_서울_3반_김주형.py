import sys
sys.stdin = open('1.txt', 'r')


T = int(input())
for tc in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    for _ in range(n):
        B = [0] * 10 #각 실행마다 이동한 정보를 저장할 배열
        if -10 < A[0] < 0: #첫요소가 음수일때
            B[0] = -A[0] #부호바꿈
        if 10 > A[0] > 0: #양수일때
            B[1] += A[0] #오른쪽이동
        if 10 > A[9] > 0: #마지막요소가 양수일때
            B[9] += -A[9] #부호바꿈
        if -10 < A[9] < 0: #마지막요소가 음수일때
            B[8] += A[9] #왼쪽이동
        if abs(A[0]) >= 10: #첫요소의 절대값이 10이상일때
            B[0] += abs(A[0])//2
            B[1] += abs(A[0])//2
        if abs(A[9]) >= 10: #마지막요쇼의 절대값이 10이상일때
            B[9] += -abs(A[9])//2
            B[8] += -abs(A[9])//2
        for i in range(1, 9): #첫과 끝을 제외한 중간 탐색
            if abs(A[i]) >= 10: #절대값 10이상일때
                B[i-1] += -abs(A[i])//2
                B[i+1] += abs(A[i])//2
            elif A[i] > 0: #양수일때
                B[i+1] += A[i]
            elif A[i] < 0: #음수일때
                B[i-1] += A[i]
        for j in range(10): #이동한 B정보를 A배열로 업데이트
            A[j] = B[j]
    print('#%d %s' % (tc+1, ' '.join(list(map(str, A)))))