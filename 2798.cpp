#include <iostream>
using namespace std;

int main(){
    int N, M;
    cin>>N>>M;
    int answer=M;
    int sum=0;
    int answer_ = 0;
    if (N>=3 && N<=100 && M>=10 && M<=300000){
        int *array = new int[N];
        for (int i=0; i<N; i++){
            cin>>array[i];
        }
        for (int i=0; i<N-2; i++){
            for (int j=i+1; j<N-1; j++){
                for (int x=j+1; x<N; x++){
                    int sum = array[i]+array[j]+array[x];
                    if ((M-sum)<answer && 0<=(M-sum)){
                        answer=M-sum;
                        answer_ = sum;
                    }
                }
            }
        }5
        delete[] array;
        printf("%d", answer_);
    }
}
