#include <iostream>
#include <algorithm>
#include <cstring>
#include <stack>
#define endl "\n"
#define ll long long
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    int m,n;
    cin >> m >> n;
    string W;
    while (1) {
        string T;
        cin >> T;
        if (T == "-1"){
            break;
        }
        W += T;
    }
    //스트링으로 변환해서 입력을 받는다, -1이 나타나면 반복문 종료

    int RawMap[n][m];
    //가로 m 세로 n 크기의 배열 형성

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            RawMap[i][j] = W[i*m + j] - 48;
            //아스키 코드를 이용한 0,1 변환
        }
    }

    int BitMap[n][m];
    //답을 구해낼 배열 하나 형성
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            BitMap[i][j] = 1;
        }
    }
    //1로 초기화



    stack<pair<int, int>> stack;
    stack.push({0,0});
    //x,y 좌표를 저장할 stack
    BitMap[0][0] = 0;
    //방문한 곳은 0

    while(!stack.empty()){
        pair <int, int> P = stack.top();
        stack.pop();
        int x = P.first;
        int y = P.second;
        BitMap[y][x] = 0;
        //스택에서 빼낸 좌표를 방문 처리
        
        if (y >= 1) {
            if ((RawMap[y - 1][x] != 1) && (BitMap[y - 1][x] != 0)) {
                stack.push({x, y - 1});
            }
            //위쪽이 갈 수 있으면 스택에 추가
        }

        if (y + 1 < n) {
            if ((RawMap[y + 1][x] != 1) && (BitMap[y + 1][x] != 0)) {
                stack.push({x, y + 1});
            }
            //아래쪽이 갈 수 있으면 스택에 추가
        }

        if (x >= 1) {
            if ((RawMap[y][x - 1] != 1) && (BitMap[y][x - 1] != 0)) {
                stack.push({x - 1, y});
            }
            //왼쪽이 갈 수 있으면 스택에 추가
        }

        if (x + 1 < m) {
            if ((RawMap[y][x + 1] != 1) && (BitMap[y][x + 1] != 0)) {
                stack.push({x + 1, y});
            }
            //오른쪽이 갈 수 있으면 스택에 추가
        }
    }

    int ans = 0;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (BitMap[i][j] == 1){
                ans++;
            }
        }
    }
    //비트맵에서 1의 개수를 카운트
    cout << ans;


}






