#include <iostream>
#include <stack>
using namespace std;

int main(){
    int K;
    cin>>K;
    stack<int> s;
    int answer = 0;
    for (int i=0; i<K; i++){
        int N;
        cin>>N;
        if (N>0 && N<1000000){
            answer += N;
            s.push(N);
        }
        else if(N==0){
            answer -= s.top();
            s.pop();
        }
    }
    cout<<answer<<endl;;
}
