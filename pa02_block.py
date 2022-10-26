import sys
input = sys.stdin.readline

L = list(map(int, input().split()))
R = list(map(int, input().split()))

L.pop()
R.pop()
#마지막 -9 제거

xlen = 0
ylen = len(L)

try :
    xindex = R.index(-1)
    #-1이 R에서 존재하는 경우 판명을 위해 try, except문 사용   
    xlen = L[xindex]

except :
    #-1이 R에서 존재하지 않는 경우 L[i]와 R[i] 값의 + 1의 최대치를 xlen으로 판정
    for i in range(len(L)):
        if (L[i] + R[i] + 1 > xlen):
            xlen = L[i] + R[i] + 1

xy = [[0 for _ in range (xlen)] for i in range (ylen)]
#보도 블럭이 하나도 설치 안된 판을 0으로 할당

for i in range (len(L)):
    end = L[i]
    for j in range (end):
        xy[i][j] = 1
#L값을 기준으로 블록을 채움

for i in range(len(R)):
    end = R[i]
    if (end == -1):
        #end가 -1이면 이미 L값으로 블록을 채운 경우니 pass
        continue
    else:
        for j in range (end):
            xy[i][xlen -1 - j] = 1
#R값을 기준으로 블록을 채움

up = []
down = []


for i in range(xlen):
    c = 0
    for j in range(ylen):
        if (xy[j][i] == 1):
            c += 1
    # 위에서 아래로 내려오면서, 1을 만날경우 c에 더해줌
      
        else:
            break
    # 0을 만난 경우 break

    up.append(c)


for i in range(xlen):
    c = 0
    for j in range(ylen):
        if (xy[ylen -1 -j][i] == 1):
            c += 1
    # 아래에서 위로 올라가면서, 1을 만날경우 c에 더해줌

        else:
            break
    # 0을 만난 경우 break


    if (c == ylen):
        down.append(-1)
    # 위, 아래로 블록이 전부 설치된 경우에는 c대신 -1을 리스트에 추가 

    else:
        down.append(c)

up.append(-9)
down.append(-9)

print(*up)
print(*down)
