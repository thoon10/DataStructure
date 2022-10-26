import sys

input = sys.stdin.readline

N = int(input())
A = [0] * 300
#일반적으로는 데크를 구현해야 하지만, 입력값이 150개라 300짜리 리스트로 감당이 되었다.
B = True
#B가 False가 되면 더 이상 앞뒤 값을 바꿀 수 없다.

FS = True
RS = True

C = (int(input().rstrip()))
A[150] = C
C = (int(input().rstrip()))
A[151] = C

#초기 두개의 값은 따로 입력 받는다.

if (A[150] < A[151]):
    A[150], A[151] = A[151], A[150]
    #왼쪽에 큰 수를 둔다.

F = 150
R = 151
#각기 프론트와 리어 값으로 준다.

for i in range (N-2):
    C = (int(input().rstrip()))

    if (B):
        if (A[F] > C > A[F+1]) and FS:
            #C의 범위가 F와 F+1일 때
            A[F-1] = C
            F -= 1
            A[F], A[F+1] = A[F+1], A[F]

            if(i != 0):
                RS = False


        elif (A[R-1] > C > A[R]) and RS:
            # C의 범위가 R-1와 R일 때
            A[R+1] = C
            R += 1
            A[R-1], A[R] = A[R], A[R-1]

            if(i != 0):
                FS = False

        elif (C > A[F]):
            # C가 F보다 클 때
            A[F-1] = C
            F -= 1
            FS = True
            RS = True


        elif (C < A[R]):
            # C가 R보다 작을 때
            A[R+1] = C
            R += 1
            FS = True
            RS = True

        else :
            #위 경우를 제외하고는, C가 열차에 붙지 않은 케이스로 B에 주기된 상태
            B = False


    else :
        if (C > A[F]):
            # C가 F보다 클 때
            A[F-1] = C
            F -= 1

        elif (C < A[R]):
            # C가 R보다 작을 때
            A[R+1] = C
            R += 1

        else:
            #열차에 붙이지 못하면 반복 종료
            break

print(len(A) - A.count(0))
#초기 설정된 길이에서 0의 개수만큼 빼주면 정답












