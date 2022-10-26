import sys, copy
input = sys.stdin.readline

def shuffle(L):
    n = int(len(L) / 2)
    if (len(L) % 2 == 0):
        L1 = copy.deepcopy(L[:n])
        L2 = copy.deepcopy(L[n:])
    # 짝수일 때
    else:
        L1 = copy.deepcopy(L[:n + 1])
        L2 = copy.deepcopy(L[n + 1:])
    # 홀수일 때
    #deepcopy를 통해, 원본 리스트를 변형 시키지 않음.

    cnt = 0
    for i in range(n):
        L[cnt] = L1[i]
        cnt += 1
        L[cnt] = L2[i]
        cnt += 1
        #카운트를 증가시키면서, 순번대로 L1, L2의 값을 L에 다시 넣어줌
    if (len(L) % 2 == 1):
        L[-1] = L1[-1]
        #L이 홀수일 경우, L1의 마지막 값을 넣어줘야 됨.

def compare(FL, SL):
    TL = copy.deepcopy(FL)
    cnt = 0

    while 1:
        shuffle(TL)
        cnt += 1
        if (TL == SL):
            return cnt
        #리스트가 동일하면 cnt를 리턴해줌
        elif (TL == FL):
            return 0
        #자기 자신과 같은 리스트로 돌아왔다는 말은, SL과 일치하지 않는다는 의미로, 0을 리턴

FL = []
SL = []
while 1:
    Temp = list(map(int, input().split()))
    if(Temp[-1] == -9):
        break
    else :
        FL += Temp

while 1:
    Temp = list(map(int, input().split()))
    if (Temp[-1] == -9):
        break
    else:
        SL += Temp

#입력을 라인 단위로 받고, 그 라인을 리스트로 임시 변환.
#임시 변환된 리스트의 마지막 값이 -9이면 루프 종료

BL = copy.deepcopy(FL)
#정렬된 리스트를 만들기 위해 deepcopy

BL.sort()

BLF = compare(BL,FL)
#FL을 만드는 데 섞은 횟수

BLS = compare(BL,SL)
#SL을 만드는 데 섞은 횟수

ans = min(compare(FL,SL), compare(SL,FL), abs(BLF-BLS))

#FL로 SL을 만드는 데 섞은 횟수, SL로 FL을 만드는 데 섞은 회수, 정열된 BL로 FL, SL을 만드는 데 섞은 횟수
#이 때, 하나라도 0이 있으면, 만들수 없다를 의미함.

if (ans == 0):
    print("NOT")
else:
    print(ans)
