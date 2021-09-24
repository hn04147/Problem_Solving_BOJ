#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(){
    int index;
    queue<int> q;

    cin>>index;
    for (int i=0; i<index; i++){
        string order;
        cin>>order;
        if (order == "push"){
            int num;
            cin>>num;
            q.push(num);
        }
        if (order == "pop"){
            if (!q.empty()){
                cout<<q.front()<<endl;
                q.pop();
            }
            else cout<<-1<<endl;
        }
        if (order == "size"){
            cout<<q.size()<<endl;
        }
        if (order == "empty"){
            if (q.empty()) cout<<1<<endl;
            else cout<<0<<endl;
        }
        if (order == "front"){
            if (!q.empty()) cout<<q.front()<<endl;
            else cout<<-1<<endl;
        }
        if (order == "back"){
            if (!q.empty()) cout<<q.back()<<endl;
            else cout<<-1<<endl;
        }
    }
}
