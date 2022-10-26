import sys
input = sys.stdin.readline


bld = []
BN = int(input())
for _ in range(BN):
    s, h, w = map(int, input().split())
    #빌딩의 정보를 받음
    bld.append([s,h,s+w])
    #빌딩의 정보를 좌표로 변환

star = []
SN = int(input())


for _ in range(SN):
    x, y = map(int, input().split())
    star.append([x,y])


"""
빌딩의 좌표를 기준으로 별이 over인지 under인지 먼저 판별
under일 경우 on인지 판별.
"""


for x, y in star:
    on = 0
    under = 0
    memory = [0, 0]
    for st, t, ed in bld:
        if (st <= x <= ed) and (0 <= y <= t):
            if (x == st) or (x == ed):
                on = 1

                if (memory == [0, 0]):
                    #추후, 두 빌딩이 겹칠 경우에 on 판별을 위해 메모리에 저장
                    memory = [st, ed]

                else:
                    #메모리에 기록이 있다는 건 on인 상태를 의미
                    if not (st == memory[0] or ed == memory[1]):
                        #현재의 시작값이 기록해둔 값이랑 같지 않거나, 끝 값이 기록해둔 값이랑 같지 않으면 언더.
                        under = 1


            elif (y == 0) or (y == t):
                on = 1
            else :
                under = 1


    if (on or under):
        if (on) and not (under):
            # on만 1일 경우 on
            print("on")
        else :
            print("under")

    else:
        print("over")





