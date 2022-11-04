import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

Old = []
OldC = 0
Child = []
Adult = []
AdultC = 0


for i in range(N):
    line = list(map(str,input().split()))

    if (0 <= int(line[1]) <= 15):
        Child.append(int(line[0]))

    elif (16 <= int(line[1]) <= 60):
        Adult.append(line)
        AdultC += 1

    else:
        Old.append(line)
        OldC += 1

#각 그룹별로 분류 후, 인원수 체크

Old = deque(Old)
Adult = deque(Adult)

#Old와 Adult 그룹의 Deque 처리

for i in range (OldC):
    if (Old[0][2] == 'M'):
        print(int(Old[0][0]))
        Old.popleft()
    else :
        Old.append(Old.popleft())

#우선도에 맞게 출력 혹은 뒤로 보냄

for i in Old:
    print(int(i[0]))

#남은 인원 출력

print(*Child, sep="\n")

#Child는 그냥 출력

for i in range (AdultC):
    if (Adult[0][2] == 'F'):
        print(int(Adult[0][0]))
        Adult.popleft()
    else :
        Adult.append(Adult.popleft())

#우선도에 맞게 출력 혹은 뒤로 보냄

for i in Adult:
    print(int(i[0]))

#남은 인원 출력






