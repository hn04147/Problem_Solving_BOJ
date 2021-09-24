#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    while (1){
        string input;
        getline(cin,input);
        stack<char> s;
        string result = "yes";
        if (input.length()>100) break;
        if (input.length() == 1 && input[0]=='.'){
            break;
        }
        else{
            for (int i=0; i<input.size(); i++){
                if (input[i] == '('){
                    s.push('(');
                }
                else if (input[i] == '['){
                    s.push('[');
                }
                else if (input[i] == ')'){
                    if (!s.empty() && s.top() == '('){
                        s.pop();
                    }
                    else{
                        result = "no";
                        break;
                    }
                }
                else if (input[i] == ']'){
                    if (!s.empty() && s.top() == '['){
                        s.pop();
                    }
                    else{
                        result = "no";
                        break;
                    }
                }
            }
        }
        cout<<result<<endl;
    }
}
