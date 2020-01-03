#include <iostream>
#include <stack>
using namespace std;

int main(){
    int index;
    cin>>index;
    for (int j=0; j<index; j++){
        stack<int> s;
        string input;
        cin>>input;
        string result = "YES";
        int trig = 0;
        int i=0;
        while (result=="YES" && i<input.size()){
            if (input[i]=='('){
                s.push(1);
            }
            else if(input[i]==')'){
                if (!s.empty()){
                    s.pop();
                }
                else {
                    result = "NO";
                }
            }
            i++;
        }
        if (result=="YES"){
            if (s.size()!=0){
                result="NO";
            }
        }
        cout<<result<<endl;
    }
}
