#include <iostream>
#include <stack>
using namespace std;

int main(){
    while (1){
        string input;
        getline(cin,input);
        stack<char> s;
        if (input=="."){
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

                }
                else if (input[i] == ']'){
                    
                }
            }
        }
    }
}
