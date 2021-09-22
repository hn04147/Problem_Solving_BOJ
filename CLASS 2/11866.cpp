#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(){
    int N, K;
    cin>>N>>K;
    vector<int> ans;
    queue<int> arr;
    for (int i=0; i<N; i++){
        arr.push(i+1);
    }

    for (int i=0; i<N; i++){
        for (int j=0; j<K-1; j++){
            int index = arr.front();
            arr.push(index);
            arr.pop();
        }
        int index = arr.front();
        ans.push_back(index);
        arr.pop();
    }

    cout<<"<";
    for (int i=0; i<N-1; i++){
        cout<<ans[i]<<", ";
    }
    cout<<ans[N-1]<<">"<<endl;
}
