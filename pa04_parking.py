import sys

input = sys.stdin.readline

K, N = map(int, input().split())

P = [0] * K
parkedCar = 0
flag = False

for _ in range (N):
    car = int(input())
    if (car > 0):
        
#입차인 경우        

        if (parkedCar == K):
            P = P + ([0] * K)
            flag = True
            K *= 2
        P[P.index(0)] = car
        parkedCar += 1
        
#주차

    
    else :
        
#출차

        if (-car in P):
            P[P.index(-car)] = 0
            parkedCar -= 1
    
    if ((K//3 >= parkedCar) and flag) :
        zero = P.count(0)
        for _ in range(zero):
            P.remove(0)
        K //= 2
        
#주차장 축소

        P = P + ([0] * (K - len(P)))


for i in range (len(P)):
    if (P[i] != 0):
        print("{} {}".format(i+1, P[i]))
