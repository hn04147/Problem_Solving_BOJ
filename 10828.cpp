#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> s;
    int index;
    cin>>index;
    for (int i=0; i<index; i++){
        string order;
        cin>>order;
        if (order == "push"){
            int num;
            cin>>num;
            s.push(num);
        }
        else if (order == "pop"){
            if (!s.empty()){
                cout<<s.top()<<endl;
                s.pop();
            }
            else{
                cout<<"-1"<<endl;
            }
        }
        else if (order == "size"){
            cout<<s.size()<<endl;
        }
        else if (order == "empty"){
            if (!s.empty()){
                cout<<"0"<<endl;
            }
            else{
                cout<<"1"<<endl;
            }
        }
        else if (order == "top"){
            if (!s.empty()){
                cout<<s.top()<<endl;
            }
            else{
                cout<<"-1"<<endl;
            }
        }
    }
}
