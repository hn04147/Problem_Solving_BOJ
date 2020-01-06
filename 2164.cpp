#include <iostream>
#include <queue>
using namespace std;

int main(){
    int index;
    cin>>index;
    queue<int> q;
    for (int i=0; i<index; i++){
        q.push(i+1);
    }
    for (int i=1; i<index; i++){
        q.pop();
        int num=q.front();
        q.pop();
        q.push(num);
    }
    cout<<q.front();
}
