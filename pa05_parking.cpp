#include <iostream>
#include <cstring>
using namespace std;
#define endl "\n"

int main() {
    int K, N;
    cin >> K >> N;
    int *P = new int [K];
    memset(P, 0, sizeof(int) * K);
    
//초기에 주차된 차가 없다는 걸 0으로 할당함

    int parkedCar = 0;
    bool flag = false;

    for (int i = 0; i < N; i++){
        int car;
        cin >> car;
        if (car > 0){
            
//입차일 경우

            if (parkedCar == K) {
                
//주차된 차와 주차장 공간이 같아지면

                int *NP = new int[K * 2];
                
//새 주차공간 할당

                memset(NP, 0, sizeof(int) * K * 2);
                
//새 주차공간 초기화


                for (int i = 0; i < K; i++) {
                    NP[i] = P[i];
                }
                
//주차된 차 옮기기

                K = K * 2;
                
//주차장 크기 확장

                delete[] P;
                
//기존 주차장 삭제

                P = NP;
                
//주차장 이름 변경

                NP = NULL;

                flag = true;
                
//초기에 주차공간이 다 찰때까지는 확장 안함.

            }

                for (int j = 0; j < K; j++) {
                    
//자리 생성 완료후 주차

                    if (P[j] == 0){
                        if (car > 0) {
                            
//주차 예정인 차면

                            P[j] = car;
                            
//주차

                            parkedCar++;
                            break;
                        }
                    }
                }



        }
        else{
            
//출차일 경우

            for (int j = 0; j < K; j++) {
                if (P[j] == -car) {
                    
//주차된 차를 발견하면

                    P[j] = 0;
                    
//출차

                    parkedCar--;
                    break;
                    }
                }
            }

        if (((K/3) >= parkedCar) && flag){
            
//주차된 차가 주차장 공간의 1/3보다 적으면

            int *NP = new int [K/2];
            
//새 주차공간 할당

            memset(NP, 0, sizeof(int) * (K/2));
            
//새 주차공간 초기화

            for (int i = 0; i < K; i++){
                if (P[i] == 0) {
                    
//i번 주차공간에 차가 없으면

                    for (int j = i + 1; j < K; j++) {
                        if (P[j] != 0){
                            P[i] = P[j];
                            P[j] = 0;
                            break;
                        }
                    }
                }
            }

            K = K / 2;
            
//주차장 크기 축소


            for (int i = 0; i < K; i++){
                NP[i] = P[i];
            }
            
//주차된 차 옮기기


            delete [] P;
            
//기존 주차장 삭제

            P = NP;
            
//주차장 이름 변경

            NP = NULL;
        }


    }

    for (int i = 0; i < K; i++){
        if (P[i] != 0){
            cout << i+1 << " " << P[i] << endl;
        }
    }

}
